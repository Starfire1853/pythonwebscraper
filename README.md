# pythonwebscraper

This is a webscraper with the purpose of texting the most recently posted workout on [https://www.crossfitmagnus.com/workouts/](https://www.crossfitmagnus.com/workouts/ "Workouts - Crossfit Magnus").
This program used BeatutifulSoup4 and html2text to parse the html and twillio to message the text.

## The following is for the test python programs (two, three and four) located in the `Test_Scrapers` subfolder.

To run this scraper2,3 and 4 you need a file called `variables.py` next to the python file, it must contain these variables:

```python
url = 'https://www.crossfitmagnus.com/workouts/'
url2 = 'https://kekoam.github.io/pythonwebscraper/'
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_phone_number = '+xxxxxxxxxxx'
my_phone_number = '+1-xxx-xxx-xxxx'
```
