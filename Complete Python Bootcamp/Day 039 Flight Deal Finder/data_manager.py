import os
import requests
import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._SHEETY_API = os.environ.get('SHEETY_API')
        self._SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
        self._SHEETY_AUTHORIZATION = ('Authorization', f'Basic {self._SHEETY_TOKEN}')
        self.sheety_endpoint = f'https://api.sheety.co/{self._SHEETY_API}/flightDeals/prices'
        self.destination_data = {}

    def get_dest_max_price(self):
        response = requests.get(url=self.sheety_endpoint)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            update_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f'{self.sheety_endpoint}/{city['id']}', json=update_data)
