from datetime import datetime as dt
import requests

API_KEY = "66609f91e4d55859907411gsv834dd8"

Lat_Long_URL = "https://geocode.maps.co/search"

Temprature_URL = "https://api.open-meteo.com/v1/forecast"
'''
?latitude=16.572090&longitude=82.000854&
current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
'''


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

   



print(lat_long('hgdufhg'))  