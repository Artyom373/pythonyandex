import requests
import json
import config
def get_city_coord(city):
    payload = {'geocode': city, 'apikey': config.geo_key, 'format': 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params = payload)
    geo = json.loads(r.text)
    #return print(geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'])
    return geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

# get_city_coord('Москва')


def get_weather(city):
    coordinates = get_city_coord(city).split()  #split преобразовывает строку в список
    payload = {'lat': coordinates[1], 'lon': coordinates[0], 'lang': 'ru_RU'}
    r = requests.get('https://api.weather.yandex.ru/v2/informers', params=payload, headers=config.weather_key)
    weather_data = json.loads(r.text)
    # return print(weather_data['fact'])
    return weather_data

# get_weather('Москва')