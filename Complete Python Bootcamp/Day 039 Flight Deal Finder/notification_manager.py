import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ.get('ACCOUNT_SID'), os.environ.get('AUTH_TOKEN'))

    def send_text(self, message_body):
        message = self.client.messages.create(from_=os.environ.get('TWILIO_NUM'), body=message_body, to=os.environ.get('ALERT_NUM'))
        print(message.status)

