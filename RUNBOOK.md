# Runbook — Global Calendar Forecast (quick start)

## 1. Build container
docker build -t global-calendar-forecast .

## 2. Fetch core datasets
python data_ingest/fetch_hurdat2.py
python data_ingest/fetch_ibtracs.py
python data_ingest/fetch_coops.py  # edit station/date in script or call function
python data_ingest/fetch_fema.py

## 3. Preprocess tide gauge JSON -> CSV
python preprocessing/tide_qc.py data/tide_gauges/8720218_20251224_20251224.json data/processed/8720218_20251224_20251224.csv

## 4. Run timing analysis (example)
python analysis/timing_analysis.py data/model_surge/example_surge.csv data/fema/declarations.json

## Notes
- Replace example inputs with your model outputs and full FEMA file.
- For full hindcasts, run spectral wave model and surge model externally and place outputs in `data/model_surge/`.
- Use ensemble assimilation (EnKF or 4D-Var) to tune drag and wave input coefficients.
