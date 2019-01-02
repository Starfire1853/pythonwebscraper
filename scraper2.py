import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client
import requests


req = requests.get(variables.url)


soup = BeautifulSoup(req.content, 'html.parser')


workoutblocks = soup.find("div", {"class": "e-content"})
# print(workoutblocks)
print("-------------------------------")
for div_tag in workoutblocks:

    workouttext = div_tag.text, div_tag.next_sibling
    # print(div_tag.text, div_tag.next_sibling)
    print(workouttext)
    client = Client(variables.account_sid, variables.auth_token)
    message = client.messages.create(
        # body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        body=workouttext,
        from_=variables.twilio_phone_number,
        to=variables.my_phone_number,
    )

print("-------------------------------")


print(message.sid)
