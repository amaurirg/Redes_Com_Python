#!/usr/bin/env python3
# Informa Latitude e Longitude usando API do Google com pygeocoder

from pygeocoder import Geocoder


if __name__ == '__main__':
    address = 'Avenida Brasil, 1000'
    # address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
