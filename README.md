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


