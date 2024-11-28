import flask
import requests
import json


from api_key import API_KEY


url_weather = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/'
url_get_location_key = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'


params_for_get_location = {
    'q': f"{52.5200},{13.4050}",
    'apikey':API_KEY
}

params_for_weather = {
    'apikey':API_KEY
}




# requests_location = requests.request(url=url_get_location_key, method='GET', params=params_for_get_location)
# location_key = requests_location.json().get('Key')
location_key = int('2515351')
request_weather = requests.request(url = url_weather + f'{location_key}/', method='GET', params=params_for_weather)

print(request_weather.json())