from datetime import datetime as dt
import requests

API_KEY = "API_KEY"

Lat_Long_URL = "https://geocode.maps.co/search"

Temprature_URL = "https://api.open-meteo.com/v1/forecast"

api_key = "API_KEY"

URL = "https://api.openweathermap.org/data/2.8/onecall"

def lat_long(city):
    response = requests.get(Lat_Long_URL, params={'q' : city, 'api_key' : API_KEY})
    response.raise_for_status()
    json_data = response.json()
    if len(json_data) != 0:
        lat = json_data[0]['lat']
        long = json_data[0]['lon']
        return lat,long
    return "city not present","city not present"


def tempertaure(city):
    lat, long = lat_long(city)
    if lat != "city not present":
        response = requests.get(Temprature_URL, params={
            'latitude' : lat,
            'longitude' : long,
            'current' : 'temperature_2m,wind_speed_10m', 'hourly' : 'temperature_2m,relative_humidity_2m,wind_speed_10m'
        })
        response.raise_for_status()
        json_data = response.json()
        time_arr = json_data['hourly']['time']
        temp_arr = json_data['hourly']['temperature_2m']

        now = dt.now()
        current_time = int(now.strftime("%H:%M:%S").split(':')[0])
        next_six_temp = temp_arr[current_time: current_time+7]

        return current_time, next_six_temp
    return [],[]

   

def rain_chance(city):
    MY_LAT,MY_LONG = lat_long(city)
    if MY_LAT != "city not present":
        
        parameters = {
            "lat" : MY_LAT,
            "lon" : MY_LONG,
            "appid" : api_key,
            "exclude" : "current,minutely,daily"
        }

        response = requests.get(url=URL, params=parameters)
        response.raise_for_status()
        weather_data = response.json()["hourly"]

        weather_hourly = weather_data[0:9]
        rain_chance = ['High' if hour['weather'][0]['id'] < 700 else 'Low' for hour in weather_hourly]

        return rain_chance
    return []

