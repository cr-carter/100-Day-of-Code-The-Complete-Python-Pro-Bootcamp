'''
The purpose of this project was to continue gaining experience with APIs. I utilized APIs from three different
sources, which involved reading through API documentation to implement the correct requests and use the returned
data. I also reinforced the usage of using environment varialbes to store and access sensitive information such as
API keys.
'''

from datetime import timedelta
import requests
import datetime
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

stock_endpoint = 'https://www.alphavantage.co/query'
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.environ.get('STOCK_API')
}

now = datetime.date.today()
yesterday = now - timedelta(1)
ereyesterday = now - timedelta(2)

request = requests.get(stock_endpoint, stock_parameters)
request.raise_for_status()
data = request.json()
yesterday_close = data["Time Series (Daily)"][str(yesterday)]["1. open"]
ereyesterday_close = data["Time Series (Daily)"][str(ereyesterday)]["1. open"]

difference = abs(float(ereyesterday_close) - float(yesterday_close)) / float(yesterday_close) * 100

if difference > 1:
    news_endpoint = 'https://newsapi.org/v2/everything'
    news_parameters = {
        'qInTitle': COMPANY_NAME,
        'from': ereyesterday,
        'apiKey': os.environ.get('NEWS_API'),
        'language': 'en'
    }

    request = requests.get(news_endpoint, news_parameters)
    request.raise_for_status()
    data = request.json()["articles"]
    articles = data[:3]

    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    twilio_num = os.environ.get('TWILIO_NUM')
    alert_num = os.environ.get('ALERT_NUM')

    if yesterday_close > ereyesterday_close:
        text_header = f"TSLA: +{round(difference, 2)}"
    else:
        text_header = f"TSLA: -{round(difference, 2)}"
    headlines = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in articles]
    client = Client(account_sid, auth_token)
    for headline in headlines:
        message = client.messages.create(
            from_=twilio_num,
            body=f"{text_header}\n{headline}",
            to=alert_num
        )
