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
repeattime = 0
repeatnumber = 0


def getrepeattime():
    global repeatnumber, repeattime
    repeatnumberin = (input("How many times should this repeat? ") or 5)
    repeattimein = (input(
        "How long between each repeat in minutes? (Equal or greater than 1 minute) ") or 1)
    if repeatnumberin < 1:
        repeatnumber = 1
    else:
        repeatnumber = int(repeatnumberin)
    if repeattimein < 1:
        repeattime = 1
    else:
        repeattime = int(repeattimein)


def getsite():
    global soup
    req = requests.get(variables.url2)
    soup = BeautifulSoup(req.content, 'html.parser')


def checkchange():
    global soup, header, checknumber
    checknumber += 1
    if checknumber >= repeatnumber:
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


getrepeattime()
schedule.every(repeattime).minutes.do(checkchange)


while 1:
    schedule.run_pending()
    time.sleep(1)
