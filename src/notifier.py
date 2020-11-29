import os
from twilio.rest import Client

class Notifier():
    def __init__(self):
        self.from_number = os.environ['TWILIO_NUMBER']

        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)
    
    def notify(self, numbers, body):
        for number in numbers:
            self.client.messages.create(body=body, from_=self.from_number, to=number)

