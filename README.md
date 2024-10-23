Application 2: Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates
Zeotap | Software Engineer Intern | Assignment | Application 2

#My Intro
Hello I'm Anvitha Guduru, a Python Full-Stack Developer skilled in React,Flak,.net,Angularjs,SQL. I'm currently working on projects like a Leave Management System, always eager to learn and innovate!
---Introduction
This project builds a Real-Time Data Processing System for Weather Monitoring with rollups and aggregates using data from OpenWeatherMap API. The system is capable of fetching real-time weather data, performing daily rollups, and triggering temperature alerts based on user-defined thresholds.

---Technical Parts
#Installation
##Backend (FastAPI):
###Install project dependencies:
poetry install
#Database (PostgreSQL):
##Start the PostgreSQL database:
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgre

---File Structure
Below is the file structure of the project:

weather_monitoring/
│
├── app.py                      # Main entry point for the FastAPI application
├── database.py                 # Database connection and session management
├── models.py                   # Database schema (WeatherData model)
├── weather_service.py          # Fetches weather data from OpenWeatherMap API
├── weather_processor.py        # Processes weather data for rollups and aggregates
├── static/
│   └── index.html              # Frontend for interacting with the system
└── .env                        # Environment variables (API keys, database URL)

---API Routes
The system uses the following FastAPI routes for handling user interactions:

/fetch_weather/ - POST: Fetches weather data for six cities from the OpenWeatherMap API and stores it in the PostgreSQL database.
/daily_summary/{city} - GET: Provides a daily summary of weather data for a specific city (including max, min, average temperatures, and dominant weather condition).
/set_threshold/ - POST: Allows users to set temperature thresholds for a specific city. If the real-time temperature exceeds the threshold, an alert is triggered.
/get_thresholds/ - GET: Fetches the current thresholds set for each city.

---About Solution
####Overview
This project solves the problem of real-time weather monitoring and data aggregation. The key features include:

# Real-time Weather Data:  Retrieves and processes weather data from OpenWeatherMap for major Indian cities.
# Daily Summaries:  Provides daily rollups (average, max, min temperature) and aggregates (dominant weather condition).
#Threshold Alerts: Users can define temperature thresholds for cities, and alerts are triggered if the threshold is breached.

----API Routes
1. /fetch_weather/
Method: POST
Description: Fetches the latest weather data for six cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) from OpenWeatherMap API. The data is processed and saved in the PostgreSQL database.
2. /daily_summary/{city}
Method: GET
Description: Provides the daily summary for a given city, including:
 Maximum temperature
 Minimum temperature
 Average temperature
 Dominant weather condition (based on frequency)
3. /set_threshold/
Method: POST
Description: Allows users to define a temperature threshold for a city. If the real-time temperature exceeds this threshold, an alert is triggered.
Payload Example:
{
  "city": "Hyderabad",
  "max_temp": 35
}
4. /get_thresholds/
Method: GET
Description: Fetches the current temperature thresholds for all cities.

-----Swagger API Documentation
FastAPI comes with built-in support for generating interactive API documentation using Swagger. This is a great tool for both development and debugging, allowing you to test your API routes directly from the browser without needing an external client like Postman.

Accessing Swagger UI: can access the Swagger UI at the following URL: http://127.0.0.1:8000/docs
#Explore API Endpoints: You will see a list of all available endpoints like /fetch_weather/, /set_threshold/, /daily_summary/{city}, etc.
#Testing the API:
Click on any API route to expand it.
For POST endpoints (like /fetch_weather/ and /set_threshold/), you can input data and test the functionality by clicking the "Try it out" button.
For GET endpoints (like /daily_summary/{city}), simply input the required parameters and click "Execute".
#View Responses: Swagger will show you the JSON response directly on the page, which is useful for quick testing and debugging.

----Data Rollups and Aggregates
1. Daily Weather Summary:
The system aggregates weather data on a daily basis for each city:

Average Temperature: Calculated from all recorded temperatures for the day.
Maximum Temperature: The highest temperature recorded for the day.
Minimum Temperature: The lowest temperature recorded for the day.
Dominant Weather Condition: Based on the frequency of weather conditions (e.g., Rain, Clear).
2. Threshold Alerts:
Users can define a temperature threshold for each city. The system continuously tracks weather updates, and if a city's temperature exceeds the set threshold, it triggers an alert, which is logged on the console.

---Non-Technical Parts
#My Approach
Step 1: Understanding Requirements: The first step was to understand the core problem: building a real-time weather monitoring system that fetches, processes, and stores weather data while providing meaningful insights.

Step 2: API Integration: I integrated the system with OpenWeatherMap API for real-time weather updates. The fetched data is processed and stored in a PostgreSQL database.

Step 3: Rollups and Aggregates: I implemented logic to aggregate weather data and perform rollups (average temperature, max temperature, dominant weather condition).

Step 4: Alerts and Thresholds: Implemented logic to allow users to set temperature thresholds for each city and trigger alerts if the threshold is breached.

----Feedback
The assignment was a great opportunity to integrate external APIs, work with real-time data processing, and perform data aggregation. The modular nature of the FastAPI backend, combined with PostgreSQL for data persistence, made the system efficient and scalable.

---Outro
This project showcases my skills in building real-time data processing systems. I look forward to any feedback and further discussions. Thank you for reviewing my work!



