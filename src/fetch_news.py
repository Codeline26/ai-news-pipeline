import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       f'apiKey={api_key}')
response = requests.get(url)
print(response.json())