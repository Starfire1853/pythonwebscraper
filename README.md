# Python Webscraper

The purpose of this webscraper is to be able to monitor a website for changes, then text a phone using twilio if any changes exist.
The program supports multiple websites and twilio accounts running at the same time.

## How to use

1. Create a `users.yaml` file that contains the website you want to scrape and the twilio account details. This can be done by running `user_init.py` from the command line and chosing `e`. Alternitivly you can create the file yourself. The file must contain the following:

   ```yaml
   User0:
   {
   element: "Elemnt to watch (ex. h1)",
   name: "Name of user",
   repeat_num: "How many times to repeat total",
   repeat_rate: "how many times in between checks in seconds",
   twilio_auth: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   twilio_phone: "+xxxxxxxxxxx",
   twilio_sid: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   url: "url to watch",
   user_phone: "+1xxxxxxxxxx",
   }
   Use1:
   {
   element: "Elemnt to watch (ex. h1)",
   name: "Name of user",
   repeat_num: "How many times to repeat total",
   repeat_rate: "how many times in between checks in seconds",
   twilio_auth: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   twilio_phone: "+xxxxxxxxxxx",
   twilio_sid: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   url: "url to watch",
   user_phone: "+1xxxxxxxxxx",
   }

   ```

   The file can have as many "users" as needed.

2. Run `webscraper.py`, it will read from the `users.yaml` file and text the phone number stored in `user_phone` when the element changes.

## Instructions for programs in the `Test_scrapers` directory

### _These programs are old and may not work correctly_

This is a webscraper with the purpose of texting the most recently posted workout on [https://www.crossfitmagnus.com/workouts/](https://www.crossfitmagnus.com/workouts/ "Workouts - Crossfit Magnus").
This program used BeatutifulSoup4 and html2text to parse the html and twillio to message the text.

### The following is for the test python programs (two, three and four) located in the `Test_Scrapers` subfolder.

To run this scraper 2, 3 and 4 you need a file called `variables.py` next to the python file, it must contain these variables:

```python
url = 'https://www.crossfitmagnus.com/workouts/'
url2 = 'https://kekoam.github.io/pythonwebscraper/'
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_phone_number = '+xxxxxxxxxxx'
my_phone_number = '+1-xxx-xxx-xxxx'
```
