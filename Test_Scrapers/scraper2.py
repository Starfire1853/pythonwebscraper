import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client
import requests
import html2text

req = requests.get(variables.url)
soup = BeautifulSoup(req.content, 'html.parser')


def texter(text):
    client = Client(variables.account_sid, variables.auth_token)
    message = client.messages.create(
        body=text,
        from_=variables.twilio_phone_number,
        to=variables.my_phone_number,
    )
    print(message.sid)


workoutblocks = soup.find("div", {"class": "e-content"}).findChildren("p")
print(workoutblocks)
print("\n \n")

newtext = str(workoutblocks)
text = html2text.html2text(newtext.replace("[", "").replace("]", ""))
text = text.replace("_", "")
print(text)

texter(text)
