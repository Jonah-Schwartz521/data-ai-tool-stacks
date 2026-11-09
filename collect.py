"""Collect one snapshot of raw job postings from Greenhouse and Lever.
Saves each board's JSON response, untouched, to data/raw/<date>/.
Run: python collect.py
"""
import csv
import json
import time
from datetime import date
from pathlib import Path

import requests

UA = "INFO4617-JobMarketResearch/0.1 (CU Boulder student project; josc6888@colorado.edu)"
PAUSE = 1.0        # seconds between requests
MAX_TRIES = 3

URLS = {
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true",
    "lever": "https://api.lever.co/v0/postings/{token}?mode=json",
}


def get_json(url):
    """GET with an identifying User-Agent, retrying on 429 and 5xx."""
    for attempt in range(1, MAX_TRIES + 1):
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=20)
        except requests.RequestException as e:
            print(f"  request failed: {e}")
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code in (429, 500, 502, 503, 504) and attempt < MAX_TRIES:
            time.sleep(2 ** attempt)   # back off: 2s, then 4s
            continue
        print(f"  HTTP {r.status_code}, skipping")
        return None


def main():
    out_dir = Path("data/raw") / date.today().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)

    with open("boards.csv") as f:
        boards = list(csv.DictReader(f))

    total = 0
    for b in boards:
        url = URLS[b["ats"]].format(token=b["board_token"])
        print(f"{b['name']} ({b['ats']})")
        data = get_json(url)
        time.sleep(PAUSE)
        if data is None:
            continue

        n = len(data["jobs"]) if b["ats"] == "greenhouse" else len(data)
        total += n
        print(f"  {n} postings")

        path = out_dir / f"{b['ats']}_{b['board_token']}.json"
        path.write_text(json.dumps(data))

    print(f"\nSaved {total} postings from {len(boards)} boards to {out_dir}")


if __name__ == "__main__":
    main()