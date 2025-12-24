#!/usr/bin/env python3
"""
Fetch FEMA disaster declarations CSV (public dataset).
"""
import requests
from pathlib import Path

OUTDIR = Path("data/fema")
OUTDIR.mkdir(parents=True, exist_ok=True)
URL = "https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries"  # paginated API

def fetch_all(output="data/fema/declarations.json"):
    r = requests.get(URL, timeout=60)
    r.raise_for_status()
    Path(output).write_bytes(r.content)
    print(f"Saved {output}")
    return Path(output)

if __name__ == "__main__":
    fetch_all()
