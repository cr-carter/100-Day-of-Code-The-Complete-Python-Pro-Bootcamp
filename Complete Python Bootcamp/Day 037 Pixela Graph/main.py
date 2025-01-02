'''
The purpose of this project was to continue working with APIs, gaining exposure to using the post, put, and delete
methods. This was a fairly straighforward project.
'''

import requests
import os
from datetime import datetime


pixela_endpoint = 'https://pixe.la/v1/users'
pixela_api_key = os.environ.get('PIXELA_API')
username = 'chasecarter'
graph_id = 'graph1'

#Create account on pixela
user_parameters = {
    'token': pixela_api_key,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)


#Create graph on pixela
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_parameters = {
    'id': graph_id,
    'name': 'Reading Graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'sora',
}
headers = {
    'X-USER-TOKEN': pixela_api_key
}
#response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
#print(response.text)

#Make a new entry on pixela
entry_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_id}'
entry_parameters = {
    'date': datetime.today().strftime('%Y%m%d'),
    'quantity': input('How many pages did you read today?'),
}
#response = requests.post(url=entry_endpoint, json=entry_parameters, headers=headers)
#print(response.text)


#Update an entry on pixela
update_date = datetime.today().strftime('%Y%m%d')
update_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_id}/{update_date}'
update_parameters = {
    'quantity': '30'
}

#response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
#print(response.text)


#Delete an entry on pixela
delete_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph_id}/{update_date}'
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)
