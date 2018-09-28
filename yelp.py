#!/home/geoff/miniconda3/bin/python
import argparse
import json
import pprint
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
from collections import OrderedDict

#API_KEY =

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
CATEGORIES_PATH = '/v3/categories'

def request(host, path, api_key, url_params=None):
    """
    returns json from API
    """

    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()

def get_categories(api_key, locale=None):
    """
    return categories of businesses. Defaults
    to all locations.
    """

    if locale:
        url_params = {
            'locale': locale.replace(' ', '+') 
        }
    else:
        url_params = None
    response_json =  request(API_HOST, CATEGORIES_PATH , api_key, url_params=url_params)
    cats = []
    for entry in response_json['categories']:
        cats.append(entry['alias'])
    data = {"data": cats}

    return data

def business_search(api_key,lat, lon, rad=1609, cat = None):
    """
    varied search for businesses
    """

    if rad > 1609:
        raise ValueError("radius can only be a max of 1 mile/1609m")
    if cat:
        url_params = {
            'latitude': lat,
            'longitude': lon,
            'radius': rad,
            'categories': cat.replace(' ', '+'),
            'limit': 10
        }
    else:
        url_params = {
            'latitude': lat,
            'longitude': lon,
            'radius': rad,
            'limit': 10
        }

    response_json = request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)

    info = []
    for entry in response_json['businesses']:
        bus = OrderedDict( [ ( "id", entry['id']),
                             ( "name", entry['name']),
                             ( "coordinates", entry['coordinates'])
                           ]
                          )
        info.append(bus)

    businesses = {"data": info}

    return businesses



def business_details(api_key, business_id):
    """
    Return details for a specific business ID
    """

    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)

if __name__ == '__main__':

    pprint.pprint(get_categories(API_KEY, 'en_US'  ))
    #pprint.pprint(business_search(API_KEY, 42.27, -83.73,cat = 'coffee'))
    #pprint.pprint(business_details(API_KEY, 'c0WpyZFR3EoEBKcoY2LZ3Q'))

