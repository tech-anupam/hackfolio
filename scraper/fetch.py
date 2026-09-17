import json
import re
import time
import argparse
from pathlib import Path

import requests

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

HACKATHONS_FILE = DATA_DIR / "hackathons.json"
PROJECTS_FILE   = DATA_DIR / "projects.json"
SEEN_FILE       = DATA_DIR / "seen.json"

BASE_URL = "https://api.devfolio.co/api"
DELAY    = 0.8

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def load_json(path: Path, default):
    if path.exists():
        with open(path, encoding="utf-8-sig") as f:
            return json.load(f)
    return default


def save_json(path: Path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get(url: str, retries: int = 3):
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code == 429:
                time.sleep(10 * (attempt + 1))
                continue
            return None
        except requests.RequestException:
            time.sleep(3)
    return None


def fetch_all_hackathons() -> list[dict]:
    hackathons = []
    page = 1
    while True:
        data = get(f"{BASE_URL}/hackathons?filter=past&page={page}")
        if not data or not data.get("result"):
            break
        hackathons.extend(data["result"])
        if page >= data.get("pages", 1):
            break
        page += 1
        time.sleep(DELAY)
    return hackathons


def fetch_hackathon_projects(slug: str) -> list[dict]:
    projects = []
    page = 1
    while True:
        data = get(f"{BASE_URL}/hackathons/{slug}/projects?page={page}")
        if not data or not data.get("result"):
            break
        projects.extend(data["result"])
        if page >= data.get("pages", 1):
            break
        page += 1
        time.sleep(DELAY)
    return projects


def fetch_project_detail(project_slug: str):
    return get(f"{BASE_URL}/projects/{project_slug}")


def fetch_project_page_fields(slug: str) -> list[dict]:
    blocks = []
    try:
        resp = requests.get(f"https://devfolio.co/projects/{slug}", headers=HEADERS, timeout=12)
        if resp.status_code == 200:
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text, re.DOTALL)
            if m:
                data = json.loads(m.group(1))
                queries = data.get("props", {}).get("pageProps", {}).get("dehydratedState", {}).get("queries", [])
                for q in queries:
                    qd = q.get("state", {}).get("data", {})
                    if isinstance(qd, dict) and "projectFieldAnswers" in qd:
                        for item in qd["projectFieldAnswers"]:
                            field_name = (item.get("project_field") or {}).get("name") or item.get("title") or ""
                            val = (item.get("value") or "").strip()
                            if val:
                                blocks.append({"title": field_name, "body": val})
    except Exception:
        pass
    return blocks


def extract_links(raw: str | None) -> list[str]:
    if not raw:
        return []
    urls = re.findall(r"https?://[^\s,\'\"<>]+", raw)
    return list(dict.fromkeys(urls))


def extract_description_blocks(proj: dict, page_fields: list[dict]) -> list[dict]:
    blocks = []
    seen_bodies = set()

    for item in page_fields:
        body = (item.get("body") or "").strip()
        if body and body not in seen_bodies:
            seen_bodies.add(body)
            blocks.append(item)

    raw_desc = proj.get("description") or []
    if isinstance(raw_desc, list):
        for block in raw_desc:
            if isinstance(block, dict):
                title = block.get("title") or block.get("heading") or ""
                body  = (block.get("body") or block.get("content") or block.get("text") or "").strip()
                if body and body not in seen_bodies:
                    seen_bodies.add(body)
                    blocks.append({"title": title, "body": str(body)})

    for track in proj.get("prize_tracks") or []:
        pt = track.get("project_tracks") or {}
        body = (pt.get("description") or "").strip()
        if body and body not in seen_bodies:
            seen_bodies.add(body)
            blocks.append({"title": track.get("name", "Track"), "body": body})

    return blocks


def extract_member_profiles(members: list[dict]) -> list[dict]:
    result = []
    for m in members:
        profiles = {}
        for p in m.get("profiles") or []:
            name = (p.get("name") or "").lower()
            val  = (p.get("user_profiles") or {}).get("value") or ""
            if val:
                profiles[name] = val
        result.append({
            "username":  m.get("username", ""),
            "name":      f"{m.get('first_name', '')} {m.get('last_name', '')}".strip(),
            "github":    profiles.get("github", ""),
            "linkedin":  profiles.get("linkedin", ""),
            "twitter":   profiles.get("twitter", ""),
        })
    return result


def run(max_new_hackathons: int = 0):
    existing_projects: dict[str, dict] = load_json(PROJECTS_FILE, {})
    seen_slugs: set[str]               = set(load_json(SEEN_FILE, []))

    print(f"State: {len(existing_projects)} projects, {len(seen_slugs)} seen hackathons", flush=True)

    all_hackathons = fetch_all_hackathons()
    print(f"Total hackathons: {len(all_hackathons)}", flush=True)
    save_json(HACKATHONS_FILE, all_hackathons)

    hackathon_map = {h["slug"]: h for h in all_hackathons}
    new_slugs = [h["slug"] for h in all_hackathons if h["slug"] not in seen_slugs]
    new_slugs.sort(key=lambda s: hackathon_map[s].get("ends_at") or "0000", reverse=True)

    if max_new_hackathons > 0:
        new_slugs = new_slugs[:max_new_hackathons]

    print(f"New hackathons to process: {len(new_slugs)}", flush=True)

    for i, hackathon_slug in enumerate(new_slugs, 1):
        meta = hackathon_map[hackathon_slug]
        print(f"[{i}/{len(new_slugs)}] {meta['name']}", flush=True)

        stubs = fetch_hackathon_projects(hackathon_slug)
        print(f"  {len(stubs)} projects found", flush=True)

        added = 0
        for stub in stubs:
            pslug = stub["slug"]
            if pslug in existing_projects:
                continue

            time.sleep(DELAY)
            wrapper = fetch_project_detail(pslug)
            if not wrapper:
                continue

            page_fields = fetch_project_page_fields(pslug)

            proj    = wrapper.get("project", {})
            members = wrapper.get("members", [])
            links   = extract_links(proj.get("links") or "")
            github  = next((l for l in links if "github.com" in l), "")
            demo    = next((l for l in links if "github.com" not in l), "")

            pictures_raw = proj.get("pictures") or ""
            picture_list = [
                f"https://assets.devfolio.co/{p.strip()}"
                for p in pictures_raw.split(",") if p.strip()
            ]

            existing_projects[pslug] = {
                "uuid":             proj.get("uuid", stub["uuid"]),
                "slug":             pslug,
                "name":             proj.get("name") or stub.get("name", ""),
                "tagline":          proj.get("tagline") or stub.get("tagline") or "",
                "platforms":        proj.get("platforms") or [],
                "hashtags":         [t["name"] for t in proj.get("hashtags") or []],
                "description":      extract_description_blocks(proj, page_fields),
                "links":            links,
                "github":           github,
                "demo":             demo,
                "video_url":        proj.get("video_url") or "",
                "pictures":         picture_list,
                "cover_img":        proj.get("cover_img") or "",
                "architecture_diagram": proj.get("architecture_diagram") or "",
                "likes":            proj.get("likes") or 0,
                "views":            proj.get("views") or 0,
                "published_at":     proj.get("published_at") or proj.get("created_at") or "",
                "team_name":        (stub.get("team") or {}).get("name") or "",
                "members":          extract_member_profiles(members),
                "hackathon_slug":   hackathon_slug,
                "hackathon_name":   meta.get("name", ""),
                "hackathon_themes": [t["name"] for t in meta.get("themes") or []],
                "devfolio_url":     f"https://devfolio.co/projects/{pslug}",
            }
            added += 1

        print(f"  Added {added} new projects", flush=True)
        seen_slugs.add(hackathon_slug)
        save_json(PROJECTS_FILE, existing_projects)
        save_json(SEEN_FILE, list(seen_slugs))
        time.sleep(DELAY)

    print(f"\nDone. Total projects: {len(existing_projects)}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-new-hackathons", type=int, default=0)
    args = parser.parse_args()
    run(max_new_hackathons=args.max_new_hackathons)
