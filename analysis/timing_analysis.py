#!/usr/bin/env python3
"""
Compute lead times between model surge thresholds and FEMA declarations.
Inputs:
 - model surge CSV: time, surge_m
 - fema declarations CSV/JSON with event date
Outputs:
 - CSV with event_id, predicted_peak_time, declaration_time, lead_hours
"""
import pandas as pd
from pathlib import Path
from datetime import datetime

def find_peak_time(surge_ts, threshold=0.5):
    # surge_ts: DataFrame with datetime index and 'surge_m'
    peaks = surge_ts[surge_ts['surge_m'] >= threshold]
    if peaks.empty:
        return None
    return peaks['surge_m'].idxmax()

def compute_lead(model_csv, fema_csv, threshold=0.5):
    model = pd.read_csv(model_csv, parse_dates=['time']).set_index('time')
    fema = pd.read_json(fema_csv)
    results = []
    for _, row in fema.iterrows():
        event_date = pd.to_datetime(row.get('declarationDate', row.get('incidentBeginDate', None)))
        # window: +/- 48 hours around event_date
        window = model.loc[event_date - pd.Timedelta(hours=72): event_date + pd.Timedelta(hours=72)]
        peak = find_peak_time(window, threshold)
        if peak is None:
            lead = None
        else:
            lead = (event_date - peak).total_seconds() / 3600.0
        results.append({
            'disasterNumber': row.get('disasterNumber'),
            'declarationDate': event_date,
            'predicted_peak_time': peak,
            'lead_hours': lead
        })
    out = pd.DataFrame(results)
    out.to_csv("analysis/lead_times.csv", index=False)
    print("Wrote analysis/lead_times.csv")
    return out

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: timing_analysis.py model_surge.csv fema_declarations.json")
    else:
        compute_lead(sys.argv[1], sys.argv[2])
