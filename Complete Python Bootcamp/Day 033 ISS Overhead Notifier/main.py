'''
The purpose of this project is to serve as an introduction to APIs. Reading API
documentation and accessing the APIs was the key focus. Multiple APIs were used
as practice.
'''


import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.253374  # Your latitude
MY_LONG = -97.734823  # Your longitude


#U Using open.notify.org api, get the current longitude and latitude of the ISS.
# Compare it to set latitude and longitude, and determine if the ISS is within
# +/- 5 degrees.
def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_above = abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5
    return iss_above


# Based on set latitude and longitude, use sunrise-sunset.org api to
# get sunrise and sunset times. Check to see if current time is before
# sunrise or after sunset.
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Chicago"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    dark = time_now.hour < sunrise or time_now.hour > sunset
    return dark


# Continuously loop until program is terminated. Check every 60 seconds to see
# if it is after sunset, and if the ISS is overhead. If both are true, then send
# an email telling recipient to look up.
while True:
    time.sleep(60)
    if is_dark() and is_above():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            my_email = 'email@gmail.com'
            my_password = 'PASSWORD'
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f'ISS is above\n\nLook up now.')
