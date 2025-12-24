#!/usr/bin/env python3
"""
Basic QC for tide gauge JSON -> timeseries CSV
"""
import json
import pandas as pd
from pathlib import Path

def json_to_df(path):
    j = json.loads(Path(path).read_text())
    if "data" in j:
        df = pd.DataFrame(j["data"])
    else:
        df = pd.DataFrame(j)
    # standardize columns if present
    if 't' in df.columns:
        df = df.rename(columns={'t':'time','v':'water_level'})
    return df

def save_csv(json_path, out_csv):
    df = json_to_df(json_path)
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time').sort_index()
    df.to_csv(out_csv)
    print(f"Wrote {out_csv}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: tide_qc.py input.json output.csv")
    else:
        save_csv(sys.argv[1], sys.argv[2])
