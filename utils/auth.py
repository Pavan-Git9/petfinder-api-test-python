import os
import requests
from dotenv import load_dotenv

# Load the correct file explicitly
load_dotenv(dotenv_path='config/config.env')

API_KEY = os.getenv("PETFINDER_API_KEY") 
API_SECRET = os.getenv("PETFINDER_API_SECRET")

def get_access_token():
    url = "https://api.petfinder.com/v2/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]
