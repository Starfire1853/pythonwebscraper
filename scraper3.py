import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client
import html2text
import schedule
import time

header = ""
checknumber = 0


def getsite():
    global soup
    req = requests.get(variables.url2)
    soup = BeautifulSoup(req.content, 'html.parser')


def message():
    print("Working")


def checkchange():
    global soup
    global header
    global checknumber
    checknumber += 1
    if checknumber >= 5:
        quit()
    oldheader = header
    getsite()
    header = soup.find_all('h1')
    print(header)
    if (header != oldheader) & (checknumber != 1):
        texter("THE WEBPAGE HEADER CHANGED!!! It was: " +
               str(oldheader) + "Now it is: " + str(header))
    else:
        print("It is the same...")


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
