from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.environ.get('API_KEY')

URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
response = requests.get(URL)
response_json = response.json()

print("1 Dolar =", response_json['conversion_rates']['BRL'], "Reais.")