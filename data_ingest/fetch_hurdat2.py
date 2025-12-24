#!/usr/bin/env python3
"""
Fetch HURDAT2 (NHC) best-track file and parse into CSV.
"""
import requests
import pandas as pd
from pathlib import Path

OUTDIR = Path("data/raw")
OUTDIR.mkdir(parents=True, exist_ok=True)
URL = "https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2024-052520.txt"

def fetch():
    r = requests.get(URL, timeout=60)
    r.raise_for_status()
    path = OUTDIR / "hurdat2.txt"
    path.write_bytes(r.content)
    print(f"Saved {path}")
    # Minimal parser: store raw file; downstream parser will harmonize
    return path

if __name__ == "__main__":
    fetch()
