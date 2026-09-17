# Contributing

Found a great project built at a hackathon that deserves a spot here? Open a PR or an issue.

## Suggest a Project

Open an issue with the title `[Project] <project name>` and include:

- Devfolio project URL
- Hackathon it was built at
- Why it belongs here

## Report a Broken Link

Open an issue with the title `[Broken] <project name>` and include the broken URL.

## Run the Scraper Locally

```bash
pip install -r scraper/requirements.txt
python scraper/fetch.py --max-new-hackathons 5
python -c "import sys; sys.path.insert(0, 'scraper'); import generate; generate.run()"
```

All contributions welcome.
