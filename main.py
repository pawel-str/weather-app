import os
from dotenv import load_dotenv
from services.fetch_weather import fetch_weather
from services.print_log import read_log

load_dotenv()

API_KEY = os.environ.get("API_KEY")
CITY = os.environ.get("CITY")

#print(API_KEY)

weather = fetch_weather(API_KEY, CITY)

print(weather)

read_log()