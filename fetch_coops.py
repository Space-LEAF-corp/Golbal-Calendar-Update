import requests
def get_tide(station, start, end):
    url = f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=water_level&station={station}&begin_date={start}&end_date={end}&datum=MLLW&units=metric&time_zone=GMT&format=json"
    return requests.get(url).json()
