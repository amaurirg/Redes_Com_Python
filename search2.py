#!/usr/bin/env python3
# Informa Latitude e Longitude usando API do Google com requests

from requests import get


def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = get(base, params=parameters)
    # print(response.content.decode('utf-8'))
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])


if __name__ == '__main__':
    geocode('Avenida Brasil, 1000')
