import requests
from bs4 import BeautifulSoup
import variables
import twilio
from twilio.rest import Client
import html2text
import schedule
import time
import os.path
import yaml


class User:
    def __init__(self, name, url, element, repeatRate, repeatNum, twilioSID, twilioAuth, twilioPhone, userPhone):
        self.name = name
        self.url = url
        self.element = element
        self.repeatRate = repeatRate
        self.repeatNum = repeatNum
        self.twilioSID = twilioSID
        self.twilioAuth = twilioAuth
        self.twilioPhone = twilioPhone
        self.userPhone = userPhone

    def iAm(self):
        print("I am " + self.name)


def UpdateChecker(url, element, repeatNum,):
    print(url, element, repeatNum)


def Messager(twilioSID, twilioAuth, twilioPhone, userPhone, message):
    print(twilioSID, twilioPhone, twilioAuth, userPhone, message)


# End of defs

if os.path.isfile("users.yaml"):
    print("its exists")
    with open("users.yaml", 'r') as yamlfile:
        yamldata = yaml.safe_load(yamlfile)
else:
    f = open("users.yaml", "a+")
    f.close


for x in yamldata["User1"].values():
    print(x)

# users = [User("User " + str(i), "url", "element " + str(i), "repeatRate " + str(i), "repeatNum" + str(i),
#               "twillioSID" + str(i), "twilioAuth" + str(i), "twilioPhone" + str(i), "userPhone" + str(i)) for i in range(15)]
# for x in users:
#     x.iAm()
#     UpdateChecker(x.url, x.element, x.repeatNum)
#     Messager(x.twilioSID, x.twilioAuth, x.twilioPhone,
#              x.userPhone, "ITS A MESSAGE")
