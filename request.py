import requests
import json
import config
def get_city_coord(city):
    payload = {'geocode': city, 'apikey': config.geo_key, 'format': 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params = payload)
    geo = json.loads(r.text)
    return print(geo)

get_city_coord('Москва')
