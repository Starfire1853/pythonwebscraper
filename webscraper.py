import schedule
import time
import yaml
import os.path
import user_init
import twilio
from twilio.rest import Client
import threading
from bs4 import BeautifulSoup
import requests
import html2text


def main():
    yaml_loader("users.yaml")
    print(time.asctime())

    for j in yaml_data:
        run_threaded(j)
        time.sleep(15)

    while True:
        schedule.run_pending()
        time.sleep(1)


def yaml_loader(users_yaml_file):
    global yaml_data
    if os.path.exists(users_yaml_file):
        print("It exists")
        with open(users_yaml_file, "r") as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)

        for j in yaml_data:
            yaml_data[j]["text"] = ""

    else:
        if (
            input(
                "Config file does not exist, it is reccomended to run user_init.py, should that be run now? (y/n)"
            )
            == "y"
        ):
            user_init.main()
        else:
            exit()


def run_threaded(user_dict_name):
    job_thread = threading.Thread(None, time_delay, args=(user_dict_name,))
    job_thread.start()


def time_delay(user_dict_name):
    schedule.every(int(yaml_data[user_dict_name]["repeat_rate"])).seconds.do(
        user_functions, user_dict_name
    )


def user_functions(user_dict_name):

    if check_changes(user_dict_name):
        return schedule.CancelJob
    print(user_dict_name)


def check_changes(user_dict_name):
    repeat_num = yaml_data[user_dict_name]["repeat_num"]
    yaml_data[user_dict_name]["repeat_num"] -= 1
    if repeat_num <= 0:
        return False

    old_text = yaml_data[user_dict_name]["text"]
    soup = get_site(user_dict_name)
    element = str(soup.find(yaml_data[user_dict_name]["element"]))

    text = html2text.html2text(element.replace("[", "").replace("]", ""))

    print(text)
    print(old_text)

    yaml_data[user_dict_name]["text"] = text

    if text != old_text:
        messager(user_dict_name, "Changed! It changed from: " + old_text + "to" + text)


def get_site(user_dict_name):
    req = requests.get(yaml_data[user_dict_name]["url"])
    soup = BeautifulSoup(req.content, "html.parser")
    return soup


def messager(user_dict_name, message):
    twilio_sid = yaml_data[user_dict_name]["twilio_sid"]
    twilio_auth = yaml_data[user_dict_name]["twilio_auth"]
    twilio_phone = yaml_data[user_dict_name]["twilio_phone"]
    user_phone = yaml_data[user_dict_name]["user_phone"]
    # print(twilio_sid, twilio_auth, twilio_phone, user_phone, message)
    client = Client(twilio_sid, twilio_auth)
    message = client.messages.create(body=message, from_=twilio_phone, to=user_phone)
    print(time.asctime())
    print(message.sid)


if __name__ == "__main__":
    main()
