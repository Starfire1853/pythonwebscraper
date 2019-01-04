import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client
import html2text
import schedule
import time
import emoji


header = ""
checknumber = 0
text = ""


def getsite():
    global soup, workoutblocks
    req = requests.get(variables.url)
    soup = BeautifulSoup(req.content, 'html.parser')
    workoutblocks = soup.find("div", {"class": "e-content"}).findChildren("p")


def message():
    print("Working")


def checkchange():
    global soup, text, workoutblocks, checknumber
    checknumber += 1
    if checknumber >= 5:
        quit()
    oldtext = text
    getsite()
    newtext = str(workoutblocks)
    text = html2text.html2text(newtext.replace("[", "").replace("]", ""))
    text = text.replace("_", "")
    print(text)
    if (text != oldtext) & (checknumber != 1):
        texter("THE WORKOUT CHANGED!!! It was: " +
               oldtext + "Now it is: " + text)
    else:
        print("It is the same... ")


def texter(text):

    client = Client(variables.account_sid, variables.auth_token)
    message = client.messages.create(
        body=text,
        from_=variables.twilio_phone_number,
        to=variables.my_phone_number,
    )
    print(message.sid)


schedule.every(1).minutes.do(checkchange)


while 1:
    schedule.run_pending()
    time.sleep(1)
