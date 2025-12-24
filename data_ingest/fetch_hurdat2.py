#!/usr/bin/env python3
"""
Fetch HURDAT2 (NHC) best-track file and parse into CSV.
"""
from pathlib import Path

OUTDIR = Path("data/raw")
OUTDIR.mkdir(parents=True, exist_ok=True)
URL = "https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2024-052520.txt"

try:
    import requests  # pyright: ignore[reportMissingModuleSource] # If unresolved, run: pip install requests
except ImportError:
    requests = None
    # The actual error handling is in the fetch() function


def fetch():
    if requests is None:
        raise ImportError("The 'requests' library is required. Install it with 'pip install requests'.")
    r = requests.get(URL, timeout=60)
    r.raise_for_status()
    path = OUTDIR / "hurdat2.txt"
    path.write_bytes(r.content)
    print(f"Saved {path}")
    # Minimal parser: store raw file; downstream parser will harmonize
    return path

if __name__ == "__main__":
    fetch()
