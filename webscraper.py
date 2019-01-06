import schedule
import time
import yaml
import os.path


def yaml_loader(users_yaml_file):
    global yaml_data
    if os.path.isfile(users_yaml_file):
        print("It exists")
        with open(users_yaml_file, "r") as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
    else:
        f = open(users_yaml_file, "a+")
        f.close
        main()


def time_delay(user_dict_name):
    schedule.every(1).minutes.do(user_functions, user_dict_name)


def user_functions(user_dict_name):
    print(user_dict_name)
    messager(
        yaml_data[user_dict_name]["twilio_sid"],
        yaml_data[user_dict_name]["twilio_auth"],
        yaml_data[user_dict_name]["twilio_phone"],
        yaml_data[user_dict_name]["user_phone"],
        "YEET, IT WORKS!",
    )


def messager(twilio_sid, twilio_auth, twilio_phone, user_phone, message):
    print(twilio_sid, twilio_auth, twilio_phone, user_phone, message)


def main():
    yaml_loader("users.yaml")
    for j in yaml_data:
        time_delay(j)
        time.sleep(15)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
