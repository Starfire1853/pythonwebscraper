import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")

    print("resultcode: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)


if __name__ == "__main___":
    main()
