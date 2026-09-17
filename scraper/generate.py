import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from categorize import categorize, ALL_CATEGORIES

ROOT          = Path(__file__).parent.parent
DATA_DIR      = ROOT / "data"
PROJECTS_FILE = DATA_DIR / "projects.json"

GITHUB_URL   = "https://github.com/tech-anupam"
IG_URL       = "https://instagram.com/tech.anupam"
REPO_URL     = "https://github.com/tech-anupam/hackfolio"

SHIELD       = "https://img.shields.io/badge"
DEVFOLIO_CLR = "4B32C3"
GITHUB_CLR   = "181717"
IG_CLR       = "E4405F"
THEME_CLR    = "0D1117"
TAG_CLR      = "555555"


def load_projects() -> dict[str, dict]:
    if not PROJECTS_FILE.exists():
        return {}
    with open(PROJECTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def enc(text: str) -> str:
    return text.replace("-", "--").replace("_", "__").replace(" ", "%20")


def badge(label: str, message: str, color: str, url: str = "", logo: str = "") -> str:
    logo_part = f"&logo={logo}&logoColor=white" if logo else ""
    img = f"![{label}]({SHIELD}/{enc(label)}-{enc(message)}-{color}?style=flat-square{logo_part})"
    return f"[{img}]({url})" if url else img


def tag_badge(tag: str) -> str:
    return f"![{tag}]({SHIELD}/{enc(tag)}-{TAG_CLR}?style=flat-square)"


def render_description(blocks: list[dict]) -> str:
    if not blocks:
        return ""
    lines = []
    for block in blocks:
        title = (block.get("title") or "").strip()
        body  = (block.get("body") or "").strip()
        if not body:
            continue
        if title:
            lines.append(f"**{title}**")
        lines.append(f"\n{body}\n")
    return "\n".join(lines)


def render_members(members: list[dict]) -> str:
    if not members:
        return ""
    parts = []
    for m in members:
        name = m.get("name") or m.get("username") or ""
        gh   = m.get("github") or ""
        if gh:
            parts.append(f"[{name}]({gh})")
        else:
            parts.append(name)
    return ", ".join(parts)


def project_block(proj: dict, show_hackathon: bool = True) -> str:
    lines = []

    name       = proj.get("name", "")
    tagline    = proj.get("tagline") or ""
    devfolio   = proj.get("devfolio_url", "")
    github     = proj.get("github", "")
    demo       = proj.get("demo", "")
    video      = proj.get("video_url", "")
    hashtags   = proj.get("hashtags", [])[:8]
    hackname   = proj.get("hackathon_name", "")
    hackslug   = proj.get("hackathon_slug", "")
    published  = proj.get("published_at", "")[:10]
    likes      = proj.get("likes") or 0
    team_name  = proj.get("team_name") or ""
    members    = proj.get("members") or []
    desc_blocks = proj.get("description") or []
    arch       = proj.get("architecture_diagram") or ""

    lines.append(f"### {name}")

    badge_row = []
    if devfolio:
        badge_row.append(badge("Devfolio", "View Project", DEVFOLIO_CLR, devfolio, "devfolio"))
    if github:
        badge_row.append(badge("GitHub", "Source Code", GITHUB_CLR, github, "github"))
    if demo:
        badge_row.append(badge("Demo", "Live", "00C853", demo, "googlechrome"))
    if video:
        badge_row.append(badge("Video", "Watch", "FF0000", video, "youtube"))
    if show_hackathon and hackname:
        badge_row.append(badge("Built at", hackname, "0052CC", f"https://{hackslug}.devfolio.co"))
    if likes:
        badge_row.append(badge("Likes", str(likes), "FF6B6B"))
    if badge_row:
        lines.append(" ".join(badge_row))

    lines.append("")

    if tagline:
        lines.append(f"> {tagline}")
        lines.append("")

    if hashtags:
        lines.append(" ".join(tag_badge(t) for t in hashtags))
        lines.append("")

    desc_text = render_description(desc_blocks)
    if desc_text:
        lines.append(desc_text)

    if arch:
        lines.append(f"**Architecture**\n\n![Architecture Diagram]({arch})\n")

    member_line = render_members(members)
    if member_line or team_name:
        team_part = f"Team **{team_name}** -- " if team_name else ""
        lines.append(f"{team_part}{member_line}")
        lines.append("")

    if published:
        lines.append(f"`{published}`")
        lines.append("")

    return "\n".join(lines)


def generate_theme_readme(slug: str, name: str, projects: list[dict]) -> str:
    sorted_projects = sorted(projects, key=lambda p: -(p.get("likes") or 0))
    lines = []

    lines.append(f"# {name}")
    lines.append("")
    lines.append(
        f"{badge('Projects', str(len(projects)), DEVFOLIO_CLR)} "
        f"{badge('GitHub', 'tech-anupam', GITHUB_CLR, GITHUB_URL, 'github')} "
        f"{badge('Instagram', 'tech.anupam', IG_CLR, IG_URL, 'instagram')}"
    )
    lines.append("")
    lines.append(f"Back to [full showcase]({REPO_URL}#readme)")
    lines.append("")
    lines.append("---")
    lines.append("")

    for proj in sorted_projects:
        lines.append(project_block(proj, show_hackathon=True))
        lines.append("---")
        lines.append("")

    lines.append(
        f"Curated by [tech-anupam]({GITHUB_URL}) "
        f"| Follow on Instagram: [@tech.anupam]({IG_URL})"
    )
    lines.append("")

    return "\n".join(lines)


def generate_main_readme(grouped: dict[str, list[dict]], total: int, updated: str) -> str:
    lines = []

    lines.append("# Hackfolio")
    lines.append("")
    lines.append(
        f"{badge('Projects', str(total), DEVFOLIO_CLR)} "
        f"{badge('Source', 'Devfolio', DEVFOLIO_CLR, 'https://devfolio.co/hackathons/past', 'devfolio')} "
        f"{badge('Updated', updated, '28A745')} "
        f"{badge('License', 'MIT', '000000')} "
        f"{badge('GitHub', 'tech-anupam', GITHUB_CLR, GITHUB_URL, 'github')} "
        f"{badge('Instagram', 'tech.anupam', IG_CLR, IG_URL, 'instagram')}"
    )
    lines.append("")
    lines.append("## Why this exists")
    lines.append("")
    lines.append(
        "Most software showcases today are flooded with AI wrappers, "
        "ChatGPT clones, and prompt engineering demos. "
        "Hackathon builders are different. "
        "They ship real things under real pressure -- hardware that bends physics, "
        "protocols that rethink how money moves, tools that make developers faster, "
        "and products built for people who actually need them. "
        "This repo collects those projects. "
        "It pulls directly from the Devfolio API, organizes by theme, "
        "and updates every 24 hours so nothing gets buried."
    )
    lines.append("")
    lines.append(
        f"Source: [devfolio.co/hackathons/past](https://devfolio.co/hackathons/past) "
        f"| Curated by [tech-anupam]({GITHUB_URL}) "
        f"| [@tech.anupam]({IG_URL}) on Instagram"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Theme navigation table
    lines.append("## Themes")
    lines.append("")
    for slug, name in ALL_CATEGORIES:
        count = len(grouped.get(slug, []))
        if count == 0:
            continue
        lines.append(
            f"- [{name}](./{slug}) "
            f"{badge('', str(count) + ' projects', THEME_CLR)}"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # All projects grouped by theme inline
    for slug, name in ALL_CATEGORIES:
        projects = grouped.get(slug, [])
        if not projects:
            continue

        sorted_projects = sorted(projects, key=lambda p: -(p.get("likes") or 0))

        lines.append(f"## [{name}](./{slug})")
        lines.append("")

        for proj in sorted_projects:
            lines.append(project_block(proj, show_hackathon=True))
            lines.append("---")
            lines.append("")

    lines.append(
        f"Curated by [tech-anupam]({GITHUB_URL}) "
        f"| Follow on Instagram: [@tech.anupam]({IG_URL})"
    )
    lines.append("")

    return "\n".join(lines)


def run():
    projects = load_projects()
    if not projects:
        print("No projects found in data/projects.json. Run fetch.py first.", flush=True)
        return

    grouped: dict[str, list[dict]] = defaultdict(list)
    for proj in projects.values():
        slug, _ = categorize(proj)
        grouped[slug].append(proj)

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total   = len(projects)

    main_readme = generate_main_readme(grouped, total, updated)
    with open(ROOT / "README.md", "w", encoding="utf-8") as f:
        f.write(main_readme)
    print(f"Written README.md ({total} projects)", flush=True)

    for slug, name in ALL_CATEGORIES:
        theme_projects = grouped.get(slug, [])
        if not theme_projects:
            continue
        theme_dir = ROOT / slug
        theme_dir.mkdir(exist_ok=True)
        content = generate_theme_readme(slug, name, theme_projects)
        with open(theme_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written {slug}/README.md ({len(theme_projects)} projects)", flush=True)

    print("Done.", flush=True)


if __name__ == "__main__":
    run()
