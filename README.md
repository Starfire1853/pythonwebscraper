# pythonwebscraper

This is a webscraper with the purpose of texting the most recently posted workout on [https://www.crossfitmagnus.com/workouts/](https://www.crossfitmagnus.com/workouts/ "Workouts - Crossfit Magnus").
This program used BeatutifulSoup4 and html2text to parse the html and twillio to message the text.

To run this program you need a file called `variables.py`, it must contain these variables:

```python
url = 'https://www.crossfitmagnus.com/workouts/'
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_phone_number = '+xxxxxxxxxxx'
my_phone_number = '+1-xxx-xxx-xxxx'
```
