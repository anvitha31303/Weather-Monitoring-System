from models import WeatherData
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from collections import Counter

def process_weather_data(city: str, db: Session):
    today = datetime.now().date()

    # Query weather data for the current day for the given city
    weather_data = db.query(WeatherData).filter(
        WeatherData.city == city,
        WeatherData.timestamp >= today
    ).all()

    if not weather_data:
        return {"message": f"No data available for {city} today."}

    # Calculate summary
    temps = [data.temp_celsius for data in weather_data]
    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    # Determine dominant weather condition
    weather_conditions = [data.main_weather for data in weather_data]
    dominant_weather = Counter(weather_conditions).most_common(1)[0][0]

    summary = {
        "city": city,
        "date": today.strftime('%Y-%m-%d'),
        "max_temp": max_temp,
        "min_temp": min_temp,
        "avg_temp": avg_temp,
        "dominant_weather": dominant_weather
    }

    return summary
