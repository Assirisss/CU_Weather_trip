from platform import uname

import flask
import requests
import json


from api_key import API_KEY
lat = 55.7558
lon = 37.6173


def get_current_weather(lat, lon):
    url_weather_cur = 'https://api.openweathermap.org/data/2.5/weather'

    params_weather_cur = {
        'appid':API_KEY,
        'lat':lat,
        'lon':lon,
        'units': 'metric'
    }
    response = requests.request(url=url_weather_cur, method='GET', params=params_weather_cur).json()
    current = dict(
    temp = response.get('main').get('temp'),
    humidity = response.get('main').get('humidity'),
    speed_wind = response.get('wind').get('speed'),
    rain = response.get('rain')
    )

    return current

def get_forecast_weather(lat, lon):
    url_weather_cur = 'https://api.openweathermap.org/data/2.5/forecast'

    params_weather_cur = {
        'appid': API_KEY,
        'lat': lat,
        'lon': lon,
        'units': 'metric'
    }
    response = requests.request(url=url_weather_cur, method='GET', params=params_weather_cur).json()
    response =response.get('list')[0]

    forecst = dict(
        temp = response.get('main').get('temp'),
        humidity = response.get('main').get('humidity'),
        speed_wind = response.get('wind').get('speed'),
        rain = response.get('pop') * 100
    )

    return  forecst

print(get_forecast_weather(lat, lon))



