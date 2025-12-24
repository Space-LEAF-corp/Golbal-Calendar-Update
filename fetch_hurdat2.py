import requests, pandas as pd
URL = "https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2024-052520.txt"
r = requests.get(URL)
open("data/hurdat2.txt","wb").write(r.content)
# parse per HURDAT2 format into DataFrame
