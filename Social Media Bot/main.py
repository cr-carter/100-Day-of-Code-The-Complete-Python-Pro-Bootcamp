#Import necessary modules
import os
from dotenv import load_dotenv
import tweepy
from atproto import Client, client_utils
import datetime
import json
import smtplib


#Load the .env file and get keys/login for APIs
load_dotenv()

X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
BLUESKY_USER = os.getenv("BLUESKY_USER")
BLUESKY_PASS = os.getenv("BLUESKY_PASS")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SEND_EMAIL = os.getenv("SEND_ADDR")


#Function to send me an email if there are errors posting.
def error_report(platform, report):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=SEND_EMAIL,
                            msg=f"There was an error posting today's quote on {platform}.\n{report}")


#Calculate the number of days since January 1 (Jan 1 is day 0)
d0 = datetime.date(datetime.date.today().year, 1, 1)
d1 = datetime.date.today()
delta = (d1 - d0).days


#Get quote of the day from the quotes.json file, based on number of days since Jan 1
#Use text_builder to properly create tags for Bluesky post. Use string with hashtags
#for X/Twitter post.
with open("quotes.json", "r") as file:
    data = json.load(file)
    quote = f'"{data["quotes"][delta]["quote"]}"\n-{data["quotes"][delta]["author"]}'

if delta % 2 == 0:
    tags = "#Python #Programming #ComputerScience #Inspiration #Quote #QuoteOfTheDay"
    text_builder = client_utils.TextBuilder()
    text_builder.text(f'{quote}\n')
    text_builder.tag('#Python', 'Python').text(' ').tag('#Programming', 'Programming').text(' ')
    text_builder.tag('#ComputerScience', 'ComputerScience').text(' ').tag('#Inspiration', 'Inspiration').text(' ')
    text_builder.tag('#Quote', 'Quote').text(' ').tag('#QuoteOfTheDay', 'QuoteOfTheDay')
else:
    tags = "#Python #Coding #ComputerScience #Motivation #Quotes #365DaysOfQuotes"
    text_builder = client_utils.TextBuilder()
    text_builder.text(f'{quote}\n')
    text_builder.tag('#Python', 'Python').text(' ').tag('#Coding', 'Coding').text(' ')
    text_builder.tag('#ComputerScience', 'ComputerScience').text(' ').tag('#Motivation', 'Motivation').text(' ')
    text_builder.tag('#Quotes', 'Quotes').text(' ').tag('#365DaysOfQuotes', '365DaysOfQuotes')


#Connect to X/Twitter, post today's quote. Send me an email for any errors.
try:
    x_client = tweepy.Client(consumer_key=X_CONSUMER_KEY, consumer_secret=X_CONSUMER_SECRET, access_token=X_ACCESS_TOKEN, access_token_secret=X_ACCESS_SECRET)
    response = x_client.create_tweet(text=f'{quote}\n{tags}')
    print(response)
except Exception as error:
    error_report("X/Twitter", repr(error))


#Connect to Bluesky, post today's quote. Send me an email for any errors.
bs_client = Client()
profile = bs_client.login(BLUESKY_USER, BLUESKY_PASS)
text_builder = client_utils.TextBuilder()
text_builder.text(f'{quote}\n')
text_builder.tag('#Python', 'Python').text(' ').tag('#Programming', 'Programming').text(' ')
text_builder.tag('#ComputerScience', 'ComputerScience').text(' ').tag('#Inspiration', 'Inspiration').text(' ')
text_builder.tag('#Quote', 'Quote').text(' ').tag('#QuoteOfTheDay', 'QuoteOfTheDay')
try:
    profile = bs_client.login(BLUESKY_USER, BLUESKY_PASS)
    response = bs_client.send_post(text=text_builder)
    print(response)
except Exception as error:
    error_report("Bluesky", repr(error))
