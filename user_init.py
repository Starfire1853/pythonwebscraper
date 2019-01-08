# This checks for a users.yaml file, then if it does not find one, will create a new file
import os
import yaml


class User:
    def __init__(
        self,
        name,
        url,
        element,
        repeat_rate,
        repeat_num,
        twilio_sid,
        twilio_auth,
        twilio_phone,
        user_phone,
    ):
        self.name = name
        self.url = url
        self.element = element
        self.repeat_rate = repeat_rate
        self.repeat_num = repeat_num
        self.twilio_sid = twilio_sid
        self.twilio_auth = twilio_auth
        self.twilio_phone = twilio_phone
        self.user_phone = user_phone

    def i_am(self):
        print("I am " + self.name)

    def as_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "element": self.element,
            "repeat_rate": self.repeat_rate,
            "repeat_num": self.repeat_num,
            "twilio_sid": self.twilio_sid,
            "twilio_auth": self.twilio_auth,
            "twilio_phone": self.twilio_phone,
            "user_phone": self.user_phone,
        }


def users(number_of_users):
    user_list = []
    user_master_dict = {}
    user_current = -1
    for x in range(number_of_users):
        print("User " + str(x))
        user_list += [
            User(
                input("Name of User: "),
                input("Url to watch: "),
                input("What element to watch for (ex. h1): "),
                input(
                    "How often do you want to repeat the check (in minutes, default is 1): "
                ),
                input("Times it repeats the check: "),
                input("Twilio SID: "),
                input("Twilio auth token: "),
                input("Twilio phone number: "),
                input("Phone to be texted (ex. +1xxxxxxxxxx): "),
            )
        ]

    for i in user_list:
        user_current += 1
        user_name = "User" + str(user_current)
        user_master_dict[user_name] = i.as_dict()

    print(user_master_dict)
    print("##############  Dumping Dict Now  ##############")
    yaml_dumper(user_master_dict)


def yaml_dumper(dict):
    yaml_file = open("users1.yaml", "w+")
    yaml.dump(dict, yaml_file)


def fill_file(change_type):
    if change_type == "a":
        print("append")
    elif change_type == "e":
        user_input = input("How many users do you want to append? ")
        users(int(user_input))
    elif change_type == "m":
        print("modify")
    elif change_type == "f":
        print("fill")


def create_file():
    print("Creating file")
    yaml_file = open("users1.yaml", "w+")
    yaml_file.close()
    fill_file("f")


def main():
    exists = os.path.isfile("user1s.yaml")
    if exists:
        print("Exists")
        fill_file(
            input(
                "Do you want to append (a), erase and refill (e) modify (m) or fill (f) the file? "
            )
        )
    else:
        print("Does not exist")
        create_file()


if __name__ == "__main__":
    main()
