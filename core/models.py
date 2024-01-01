from django.db import models
from twilio.rest import Client
import os

class Score(models.Model):
    result = models.IntegerField()

    def __str__(self):
        return str(self.result)
    
    def save(self, *args, **kwargs):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        if self.result < 70:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=f" Your score is low: {self.result}",
                                from_=os.environ['TWILIO_SENDER'],
                                to=os.environ['TWILIO_RECEIVER']
                            )

            print(message.sid)
        return super().save(*args, **kwargs)
