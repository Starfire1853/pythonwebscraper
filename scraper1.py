import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client

client = Client(variables.account_sid, variables.auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_=variables.twilio_phone_number,
    to=variables.my_phone_number,
)

print(message.sid)
