import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client
import requests
import html2text

req = requests.get(variables.url)
soup = BeautifulSoup(req.content, 'html.parser')
workoutblocks = soup.find("div", {"class": "e-content"}).findChildren("p")
print(workoutblocks)


newtext = str(workoutblocks)
# print(newtext.replace("<br/>", "\n"))
print("-------------------------------")

text = html2text.html2text(newtext.replace("[", "").replace("]", ""))
print(text)
print("-------------------------------")
text = text.replace("_", "")
print(text)

client = Client(variables.account_sid, variables.auth_token)
message = client.messages.create(
    # body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    body=(" \n" + text),
    from_=variables.twilio_phone_number,
    to=variables.my_phone_number,
)
print(message.sid)
# for div_tag in workoutblocks:

#     workouttext = div_tag.text
#     # print(div_tag.text, div_tag.next_sibling)
#     print(workouttext)
#     print("-------------------------------")
#     print(workouttext.replace("A", "A\n"))
#     print("-------------------------------")
#     ftext = workouttext.replace(" B.", "\n B.")
#     ftext2 = ftext.replace(" C.", "\n C.")

#     client = Client(variables.account_sid, variables.auth_token)
#     message = client.messages.create(
#         # body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#         body=ftext2,
#         from_=variables.twilio_phone_number,
#         to=variables.my_phone_number,
#     )


# print("-------------------------------")
# print(message.sid)
