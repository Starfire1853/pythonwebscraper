import requests
from bs4 import BeautifulSoup
import twilio
from twilio.rest import Client
import html2text
import schedule
import time
import os.path
import yaml


# class User:
#     def __init__(self, name, url, element, repeatRate, repeatNum, twilioSID, twilioAuth, twilioPhone, userPhone):
#         self.name = name
#         self.url = url
#         self.element = element
#         self.repeatRate = repeatRate
#         self.repeatNum = repeatNum
#         self.twilioSID = twilioSID
#         self.twilioAuth = twilioAuth
#         self.twilioPhone = twilioPhone
#         self.userPhone = userPhone

#     def iAm(self):
#         print("I am " + self.name)


def UpdateChecker(url, element, repeatNum):
    print(url, element, repeatNum)


def Messager(twilioSID, twilioAuth, twilioPhone, userPhone, message):
    print(twilioSID, twilioPhone, twilioAuth, userPhone, message)


def user_functions(user_dict_name):
    print(user_dict_name)
    Messager(
        yamldata[user_dict_name]["twilioSID"],
        yamldata[user_dict_name]["twilioAuth"],
        yamldata[user_dict_name]["twilioPhone"],
        yamldata[user_dict_name]["userPhone"],
        "YEET, IT WORKS!",
    )


def time_delay(user_dict_name):
    schedule.every(1).minutes.do(user_functions, user_dict_name)


# End of defs

# opens the yaml user file and reads it into a dict
if os.path.isfile("users.yaml"):
    print("its exists")
    with open("users.yaml", "r") as yamlfile:
        yamldata = yaml.safe_load(yamlfile)
else:
    f = open("users.yaml", "a+")
    f.close

for j in yamldata:
    time_delay(j)
    time.sleep(15)


# print(yamldata["User1"]["element"])


# users = [User("User " + str(i), "url", "element " + str(i), "repeatRate " + str(i), "repeatNum" + str(i),
#               "twillioSID" + str(i), "twilioAuth" + str(i), "twilioPhone" + str(i), "userPhone" + str(i)) for i in range(15)]
# for x in users:
#     x.iAm()
#     UpdateChecker(x.url, x.element, x.repeatNum)
#     Messager(x.twilioSID, x.twilioAuth, x.twilioPhone,
#              x.userPhone, "ITS A MESSAGE")


while True:
    schedule.run_pending()
    time.sleep(1)
