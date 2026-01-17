import os
from dotenv import load_dotenv
import requests

"""
To test API connection.
"""
# Pull API key from .env
load_dotenv()
api_key = os.getenv("CONGRESS_API_KEY")

url = f"https://api.congress.gov/v3/bill/119?api_key={api_key}&format=json"
response = requests.get(url)

print(response.status_code)
print(response.json())