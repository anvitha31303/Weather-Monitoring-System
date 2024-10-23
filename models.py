from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from pydantic import BaseModel

class Threshold(BaseModel):
    city: str
    max_temp: float

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    main_weather = Column(String)
    temp_celsius = Column(Float)
    feels_like = Column(Float)
    timestamp = Column(DateTime)



