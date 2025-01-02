'''
The purpose of this project was to continue exploring APIs. This project incorporated
the use of Google Sheets, using an API to add data to a spreadsheet.
I also gained further experience with interpreting API results and formatting the data
to input into a second API. Care was also taken to use environment variables to avoid
coding any sensitive information into the program.
'''
import requests
import os
from datetime import datetime

#Set nutritionix.com endpoint, app id and api key
NUTRITION_APP_ID = os.environ.get("NUT_APP_ID")
NUTRITION_API_KEY = os.environ.get("NUT_API_KEY")
nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

#Set personal details for nutritionix
GENDER = 'male'
WEIGHT_KG = '86'
HEIGHT_CM = '185'
AGE = '30'

#Get exercise
exercise_type = input("Tell me which exercise you did: ")

#Create header and parameters for nutritionix api call
header = {
    'x-app-id': NUTRITION_APP_ID,
    'x-app-key': NUTRITION_API_KEY
}
parameters = {
    'query': exercise_type,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}
response = requests.post(url=nutrition_endpoint, headers=header, json=parameters)
results = response.json()

#Get todays date and the current time
todays_date = datetime.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime('%X')

#Set sheety.co api key, username, password, and endpoint
SHEETY_API = os.environ.get('SHEETY_API')
SHEETY_USER = os.environ.get('SHEETY_USER')
SHEETY_PASSWORD = os.environ.get('SHEETY_PASSWORD')
sheety_endpoint = f'https://api.sheety.co/{SHEETY_API}/myWorkouts/workouts'

#Set authentication for worksheet
sheety_auth = (SHEETY_USER, SHEETY_PASSWORD)

#Create entry for worksheet for each exercise performed
for exercise in results['exercises']:
    workout_input = {
        'workout': {
            'date': todays_date,
            'time': current_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=workout_input, auth=sheety_auth)
