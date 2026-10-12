from blockext import *
import requests

@reporter("%m.weather in %s")

def get_weather_data(wInput, city):
    # 1. Using Geocoding API URL and endpoint
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&format=json"
    geo_res = requests.get(geo_url).json()

    if "results" in geo_res and len(geo_res["results"]) > 0:
        location = geo_res["results"][0]
        lat, lon = location["latitude"], location["longitude"]
        
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m", # API expects a comma-separated string
            "timezone": "auto"
        }
        
        weather_res = requests.get(weather_url, params=params).json()
        
        # Guard clause in case 'current' key is missing in weather API response
        if "current" not in weather_res:
            return "Weather data unavailable"
            
        current = weather_res["current"]
        
        # 2. returning the weather
        if wInput == "temperature":
            return f"{current['temperature_2m']}"
        elif wInput == "humidity":
            return f"{current['relative_humidity_2m']}"
        elif wInput == "wind speed":
            return f"{current['wind_speed_10m']}"
        else:
            return "Invalid weather input type"
    else:
        return " "

menu("weather", ["temperature", "humidity", "wind speed"])

run("Weather Extension", "weather", 12345)

