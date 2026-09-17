from __future__ import annotations

CATEGORIES: list[tuple[str, str, list[str]]] = [
    (
        "web3-blockchain",
        "Web3 and Blockchain",
        [
            "blockchain", "ethereum", "solidity", "web3", "defi", "nft", "ipfs",
            "smart contract", "polygon", "dao", "crypto", "token", "wallet",
            "zk", "layer2", "l2", "aptos", "sui", "near", "avalanche",
        ],
    ),
    (
        "hardware-iot",
        "Hardware and IoT",
        [
            "hardware", "raspberry pi", "arduino", "iot", "embedded", "fpga",
            "microcontroller", "sensor", "robotics", "firmware", "esp32",
            "circuit", "pcb", "drone", "wearable",
        ],
    ),
    (
        "health-biotech",
        "Health and Biotech",
        [
            "health", "medical", "biotech", "genomics", "mental health",
            "telemedicine", "hospital", "patient", "clinical", "diagnosis",
            "fitness", "wellness", "pharma", "drug", "biology",
        ],
    ),
    (
        "climate-sustainability",
        "Climate and Sustainability",
        [
            "climate", "sustainability", "energy", "carbon", "agriculture",
            "environment", "green", "solar", "wind", "waste", "water",
            "recycl", "emission", "eco", "forest", "biodiversity",
        ],
    ),
    (
        "devtools-infrastructure",
        "DevTools and Infrastructure",
        [
            "devtools", "cli", "sdk", "compiler", "observability", "monitoring",
            "cicd", "ci/cd", "pipeline", "deployment", "kubernetes", "docker",
            "infrastructure", "database", "orm", "api gateway", "proxy",
            "debug", "profil", "testing", "lint",
        ],
    ),
    (
        "social-education",
        "Social Impact and Education",
        [
            "education", "edtech", "accessibility", "community", "social impact",
            "learning", "school", "student", "teacher", "nonprofit",
            "disability", "inclusion", "rural", "literacy", "language",
        ],
    ),
    (
        "gaming-ar-vr",
        "Gaming, AR, and VR",
        [
            "game", "gaming", "ar", "vr", "xr", "unity", "unreal", "3d",
            "metaverse", "augmented reality", "virtual reality", "simulation",
            "multiplayer", "puzzle", "shader",
        ],
    ),
    (
        "finance-fintech",
        "Finance and Fintech",
        [
            "finance", "fintech", "payment", "banking", "insurance",
            "lending", "credit", "invoice", "accounting", "tax",
            "trading", "stock", "investment", "budget", "expense",
        ],
    ),
    (
        "ai-ml",
        "AI and Machine Learning",
        [
            "machine learning", "deep learning", "nlp", "computer vision",
            "neural network", "llm", "transformer", "diffusion", "gpt",
            "bert", "stable diffusion", "yolo", "tensorflow", "pytorch",
            "opencv", "huggingface", "langchain",
        ],
    ),
]

FALLBACK_SLUG = "open-source-builds"
FALLBACK_NAME = "Open Source Builds"


def categorize(project: dict) -> tuple[str, str]:
    tokens = set()
    for tag in project.get("hashtags", []):
        tokens.add(tag.lower())
    for theme in project.get("hackathon_themes", []):
        tokens.add(theme.lower())
    text = f"{project.get('name', '')} {project.get('tagline', '')}".lower()

    for slug, name, keywords in CATEGORIES:
        for kw in keywords:
            if kw in tokens or kw in text:
                return slug, name

    return FALLBACK_SLUG, FALLBACK_NAME


ALL_CATEGORIES: list[tuple[str, str]] = [(s, n) for s, n, _ in CATEGORIES] + [
    (FALLBACK_SLUG, FALLBACK_NAME)
]
