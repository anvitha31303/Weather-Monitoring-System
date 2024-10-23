import os
import requests
from datetime import datetime
from database import get_db
from models import WeatherData
from sqlalchemy.orm import Session

API_KEY = os.getenv("API_KEY")
cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather_data():
    weather_records = []
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp_celsius = data["main"]["temp"] - 273.15
            feels_like = data["main"]["feels_like"] - 273.15
            main_weather = data["weather"][0]["main"]

            db = next(get_db())
            weather_data = WeatherData(
                city=city,
                main_weather=main_weather,
                temp_celsius=temp_celsius,
                feels_like=feels_like,
                timestamp=datetime.now()
            )
            db.add(weather_data)
            db.commit()
            weather_records.append({
                "city": city,
                "main_weather": main_weather,
                "temp_celsius": temp_celsius,
                "feels_like": feels_like,
                "timestamp": str(datetime.now())
            })
        else:
            print(f"Error fetching weather data for {city}: {data.get('message')}")

    return weather_records
