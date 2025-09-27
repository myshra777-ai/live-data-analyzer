import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
import pandas as pd
import os

API_KEY = "7133fbe71031b8f3477ee4b3caf6b86a"

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_to_csv(city, timestamp, temp, condition, wind)

        result = f"[{timestamp}] {city}: {temp}°C, {condition}, Wind: {wind} m/s"
        messagebox.showinfo("Weather Info", result)
    else:
        messagebox.showerror("Error", f"Failed to fetch weather for {city}")

def save_to_csv(city, timestamp, temp, condition, wind):
    df = pd.DataFrame([{
        "city": city,
        "timestamp": timestamp,
        "temperature": temp,
        "condition": condition,
        "wind_speed": wind
    }])
    df.to_csv("weather_data.csv", mode='a', header=not os.path.exists("weather_data.csv"), index=False)

# GUI setup
root = tk.Tk()
root.title("Weather Checker")

tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

def on_check():
    city = city_entry.get().strip()
    if city:
        fetch_weather(city)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

tk.Button(root, text="Check Weather", command=on_check).pack(pady=10)

root.mainloop()