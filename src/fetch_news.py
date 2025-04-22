import os
from dotenv import load_dotenv
import requests

def fetch_news():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = (f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}')
    response = requests.get(url).json()
    return response