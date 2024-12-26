'''
The purpose of this project was to gain further experience using APIs. This involved
reading through API documentation and understanding what data is needed and how to
isolate that data. I also worked with twilio as a way to send text alerts, supplementing
the email alerts I learned in previous days.
I also gained experience in setting and using environment variables in order to not have
variables such as api keys, account ids, auth tokens, and phone numbers hard coded.
'''

import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
owm_api_key = os.environ.get('OWM_API_KEY')
twilio_num = os.environ.get('TWILIO_NUM')
alert_num = os.environ.get('ALERT_NUM')

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
parameters = {
    "q": "Austin,US",
    "appid": owm_api_key,
    "cnt": 4
}

request = requests.get(OWM_endpoint, params=parameters)
request.raise_for_status()
weather_data = request.json()

rain = False
for hour in weather_data["list"]:
    if hour["weather"][0]["id"] < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_num,
        body="It's going to rain today. Remember to bring an umbrella",
        to=alert_num
    )
    print(message.status)
