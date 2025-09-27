import requests
import logging
from datetime import datetime
import pandas as pd

def save_to_csv(timestamp, temp, condition, wind):
    df = pd.DataFrame([{
        "timestamp": timestamp,
        "temperature": temp,
        "condition": condition,
        "wind_speed": wind
    }])
    df.to_csv("weather_data.csv", mode='a', header=not pd.io.common.file_exists("weather_data.csv"), index=False)


# Setup logging
logging.basicConfig(filename="weather_log.txt", level=logging.INFO, format="%(asctime)s | %(message)s")

# Your actual API key
API_KEY = "7133fbe71031b8f3477ee4b3caf6b86a"
CITY = "Indore"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()

    print("Status Code:", response.status_code)
    print("Response:", data)

    if response.status_code == 200:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_csv(timestamp, temp, condition, wind)

        print(f"[{timestamp}] Weather in {CITY}: {temp}°C, {condition}, Wind: {wind} m/s")
        logging.info(f"{CITY} | {temp}°C | {condition} | Wind: {wind} m/s")
    else:
        print("Failed to fetch weather data.")
        logging.error(f"API request failed: {data}")

fetch_weather()