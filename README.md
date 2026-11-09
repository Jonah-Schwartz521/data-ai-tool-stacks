# Tool Stacks Across Data and AI Roles

**Jonah Schwartz** · INFO 4617 Web Data Science · Final Project

Which tools and skills show up most in data analyst, data scientist, and AI/ML job postings at tech companies, and how much do those three roles' tool stacks overlap? I collect published postings from the public Greenhouse and Lever job board APIs in weekly snapshots from Oct 25 through Nov 29, 2026, classify each posting's role from its title, and match tools like SQL, Python, Tableau, Spark, dbt, cloud platforms, and LLM frameworks with a keyword dictionary. The goal is a share-of-postings comparison across roles plus an overlap score for each role pair, so students can see whether analyst and AI tracks really need different preparation. Full proposal: [proposal.md](proposal.md).

## Data

**Source.** Public job board APIs from Greenhouse (`boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true`) and Lever (`api.lever.co/v0/postings/{token}?mode=json`) for 29 tech and health tech companies listed in [boards.csv](boards.csv) (24 Greenhouse, 5 Lever). No keys or HTML scraping.

**Collection.** [collect.py](collect.py) requests each board once with a User-Agent naming the project and my CU email, pauses 1 second between requests, retries with backoff on 429/5xx, and saves each response untouched to `data/raw/<date>/`. First snapshot collected Nov 8, 2026; weekly snapshots continue through Nov 29.

**Records.** The Nov 8 snapshot has 4,620 postings. 267 fall in the three target roles: 142 AI/ML, 71 data science, 54 analyst.

**Cleaning.** [analysis.ipynb](analysis.ipynb) merges both sources into one table, strips HTML, replaces emails and phone numbers, classifies role from title, and dedupes by job ID across snapshots. Field definitions: [data/README.md](data/README.md).

**Left out of the repo.** `data/raw/` and `data/clean/` are gitignored. The full files are large (hundreds of full job descriptions per board), some descriptions name recruiters or include their contact info, and the posting text belongs to the companies, so republishing it in full isn't appropriate. The repo includes a 20-row sample, [data/sample_postings.csv](data/sample_postings.csv), with descriptions cut to 300 characters. Running `python collect.py` and then the notebook rebuilds everything.

## Methods
Coming soon.

## Findings
Coming soon.

## How to reproduce
Coming soon. The collector code lives in [job-market](https://github.com/Jonah-Schwartz521/job-market).
