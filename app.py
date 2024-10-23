import os
from dotenv import load_dotenv
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.background import BackgroundScheduler
from database import get_db
from models import WeatherData, Threshold
from weather_service import fetch_weather_data
from weather_processor import process_weather_data

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()
thresholds = {}

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html") as f:
        return f.read()


@app.post("/fetch_weather/")
async def fetch_and_process_weather():
    try:
        weather_data = fetch_weather_data()  # Fetch weather data directly
        return {"message": "Weather data fetching completed.", "data": weather_data}
    except Exception as e:
        return {"error": str(e)}


@app.get("/daily_summary/{city}")
def get_daily_summary(city: str):
    db = next(get_db())
    # Fetch all weather data for the specified city
    weather_data = db.query(WeatherData).filter(WeatherData.city == city).all()

    # If no data is found, raise an HTTP 404 error
    if not weather_data:
        raise HTTPException(status_code=404, detail=f"No weather data found for {city}")

    # Calculate daily aggregates
    avg_temp = sum([wd.temp_celsius for wd in weather_data]) / len(weather_data)
    max_temp = max([wd.temp_celsius for wd in weather_data])
    min_temp = min([wd.temp_celsius for wd in weather_data])
    dominant_weather = max(set([wd.main_weather for wd in weather_data]),
                           key=[wd.main_weather for wd in weather_data].count)

    return {
        "city": city,
        "avg_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "dominant_weather": dominant_weather,
        "timestamp": weather_data[0].timestamp
    }


# Initialize the background scheduler
scheduler = BackgroundScheduler()


# Function to start periodic weather fetching
def start_scheduler():
    scheduler.add_job(fetch_weather_data, 'interval', minutes=5)
    scheduler.start()


# Run the scheduler when the FastAPI app starts
@app.on_event("startup")
def on_startup():
    start_scheduler()

@app.get("/get_thresholds/")
async def get_thresholds():
    return thresholds  # Return the current thresholds dictionary

# Add a new route to set thresholds
@app.post("/set_threshold/")
async def set_threshold(threshold: Threshold, background_tasks: BackgroundTasks):
    # Store user-defined thresholds in a dictionary
    thresholds[threshold.city] = threshold.max_temp
    background_tasks.add_task(track_thresholds, threshold.city, threshold.max_temp)
    return {"message": f"Threshold set for {threshold.city} at {threshold.max_temp}°C"}



# Function to track temperature and trigger alerts
def track_thresholds(city: str, max_temp: float):
    db = next(get_db())
    weather_data = db.query(WeatherData).filter(WeatherData.city == city).order_by(WeatherData.timestamp.desc()).first()

    if weather_data and weather_data.temp_celsius > max_temp:
        print(f"ALERT: {city} has exceeded the threshold with a temperature of {weather_data.temp_celsius}°C.")
        # Additional alert mechanisms can be added here (e.g., email alerts)
