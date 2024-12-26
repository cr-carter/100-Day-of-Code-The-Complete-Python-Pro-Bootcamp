import os
import requests
from datetime import datetime

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._AMADEUS_API = os.environ.get('AMADEUS_API')
        self._AMADEUS_SECRET = os.environ.get('AMADEUS_SECRET')
        self._TOKEN = self._get_new_token()


    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._AMADEUS_API,
            'client_secret': self._AMADEUS_SECRET
        }
        response = requests.post(url='https://test.api.amadeus.com/v1/security/oauth2/token', headers=header, data=body)
        return response.json()['access_token']

    def get_iata_code(self, city_name):
        headers = {'Authorization': f'Bearer {self._TOKEN}'}
        query = {
            'keyword': city_name,
            'max': '2',
            'include': 'AIRPORTS'
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        try:
            iata_code = response.json()['data'][0]['iataCode']
            return iata_code
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not Found"

    def flight_checker(self, origin_code, destination_code, from_date, to_date):
        headers = {'Authorization': f'Bearer {self._TOKEN}'}
        query = {
            'originLocationCode': origin_code,
            'destinationLocationCode': destination_code,
            'departureDate': from_date.strftime('%Y-%m-%d'),
            'returnDate': to_date.strftime('%Y-%m-%d'),
            'adults': 1,
            'currencyCode': 'USD',
            'max': '10'
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        return response.json()
