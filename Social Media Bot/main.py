#Import necessary modules
import json
import os
import datetime
import smtplib
from dotenv import load_dotenv
from atproto import Client, client_utils
import tweepy


#Load the .env file and get keys/login for APIs
load_dotenv()

X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
BLUESKY_USER = os.getenv("BLUESKY_USER")
BLUESKY_PASS = os.getenv("BLUESKY_PASS")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SEND_EMAIL = os.getenv("SEND_ADDR")


#Calculate the number of days since January 1 (Jan 1 is day 0)
d0 = datetime.date(2025, 1, 1)
d1 = datetime.date.today()
delta = (d1 - d0).days


#Get quote of the day from the quotes.json file, based on number of days since Jan 1
with open("quotes.json", "r") as file:
    data = json.load(file)
    quote = f'{data["quotes"][delta]["quote"]}\n-{data["quotes"][delta]["author"]}'


#Function to send me an email if there are errors posting.
def error_report(platform, report):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=SEND_EMAIL,
                            msg=f"There was an error posting today's quote on {platform}.\n{report}")


#Connect to Bluesky, post today's quote. Send me an email for any errors.
bs_client = Client()
try:
    profile = bs_client.login(BLUESKY_USER, BLUESKY_PASS)
    post = bs_client.send_post(quote)
except Exception as error:
    error_report("Bluesky", repr(error))


#Connect to X/Twitter, post today's quote. Send me an email for any errors.
try:
    x_client = tweepy.Client(X_BEARER_TOKEN, X_CONSUMER_KEY, X_CONSUMER_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET)
    response = x_client.create_tweet(text=quote)
    print(response)
except Exception as error:
    error_report("X/Twitter", repr(error))

