# Data

`sample_postings.csv` is a 20-row sample of the cleaned dataset (target roles only, descriptions cut to 300 characters). The full raw and cleaned files are not in the repo; see the main README.

## Data dictionary

| Field | Type | Meaning |
|---|---|---|
| job_id | string | Posting ID from the source, prefixed `gh_` (Greenhouse) or `lv_` (Lever). Unique key, used to dedupe across snapshots |
| company | string | Company name (Greenhouse `company_name`; Lever board slug) |
| ats | string | Source job board API: `greenhouse` or `lever` |
| title | string | Job title as posted |
| location | string | Location as posted (free text, not standardized) |
| posted_at | date | Date the posting was first published (Greenhouse `first_published`, Lever `createdAt`), UTC |
| description | string | Full posting text with HTML stripped; emails replaced with `[email]` and phone numbers with `[phone]` |
| url | string | Link to the posting |
| role | string | Role from title regex: `ai_ml`, `data_science`, `analyst`, or `other`. First match wins in that order |
| first_seen | date | First weekly snapshot the posting appeared in |
| last_seen | date | Most recent snapshot the posting appeared in |
| n_snapshots | int | Number of weekly snapshots the posting appeared in |