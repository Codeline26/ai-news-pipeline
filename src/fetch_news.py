import os
from dotenv import load_dotenv
import requests

def fetch_news():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       f'apiKey={api_key}')
    response = requests.get(url)
    return response

