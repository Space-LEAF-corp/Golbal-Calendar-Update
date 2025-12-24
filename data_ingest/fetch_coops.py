#!/usr/bin/env python3
"""
Fetch NOAA CO-OPS tide gauge water level for a station and date range.
Simple wrapper for the NOAA API.
"""
import requests # pyright: ignore[reportMissingModuleSource]
import json
from pathlib import Path
from datetime import datetime, timezone

OUTDIR = Path("data/tide_gauges")
OUTDIR.mkdir(parents=True, exist_ok=True)

def get_tide(station, begin_yyyymmdd, end_yyyymmdd, product="water_level"): # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
    url = (
        "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
        f"?product={product}&station={station}&begin_date={begin_yyyymmdd}"
        f"&end_date={end_yyyymmdd}&datum=MLLW&units=metric&time_zone=GMT&format=json"
    )
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    data = r.json()
    out = OUTDIR / f"{station}_{begin_yyyymmdd}_{end_yyyymmdd}.json"
    out.write_text(json.dumps(data))
    print(f"Saved {out}")
    return out

if __name__ == "__main__":
    # example: station 8720218 (Key West) for one day
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    get_tide("8720218", today, today)
