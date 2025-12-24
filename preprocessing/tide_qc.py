#!/usr/bin/env python3
"""
Basic QC for tide gauge JSON -> timeseries CSV
"""
import json
import pandas as pd # pyright: ignore[reportMissingModuleSource]
from pathlib import Path

def json_to_df(path: str) -> pd.DataFrame:
    j = json.loads(Path(path).read_text())
    if "data" in j:
        df: pd.DataFrame = pd.DataFrame(j["data"])
    else:
        df: pd.DataFrame = pd.DataFrame(j)
    # standardize columns if present
    if 't' in df.columns:
        df = df.rename(columns={'t':'time','v':'water_level'}) # pyright: ignore[reportUnknownMemberType]
    return df

def save_csv(json_path: str, out_csv: str):
    df: pd.DataFrame = json_to_df(json_path)
    df['time'] = pd.to_datetime(df['time']) # pyright: ignore[reportUnknownMemberType]
    df: pd.DataFrame = df.set_index('time') # pyright: ignore[reportUnknownMemberType]
    df = df.sort_index() # pyright: ignore[reportUnknownMemberType]
    df.to_csv(str(out_csv)) # pyright: ignore[reportUnknownMemberType]
    print(f"Wrote {out_csv}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: tide_qc.py input.json output.csv")
    else:
        save_csv(sys.argv[1], sys.argv[2])
