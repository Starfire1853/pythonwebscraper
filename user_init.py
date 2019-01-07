# This checks for a users.yaml file, then if it does not find one, will create a new file
import os


def fill_file(append, erase, modify):
    pass


def create_file():
    print("Creating file")
    yaml_file = open("user1s.yaml", "w+")

    yaml_file.close()


def main():
    exists = os.path.isfile("user1s.yaml")
    if exists:
        print("Exists, running webscraper.py")
    else:
        print("Does not exist")
        create_file()


if __name__ == "__main__":
    main()
