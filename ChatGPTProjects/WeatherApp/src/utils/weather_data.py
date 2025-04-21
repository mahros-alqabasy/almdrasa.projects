# src/utils/weather_data.py

from dataclasses import dataclass

@dataclass
class ValueModel:
    value: object
    unit: str

@dataclass
class Units:
    windspeed: str
    winddirection: str

@dataclass
class WeatherData:
    temp: ValueModel
    windspeed: ValueModel
    winddirection: ValueModel
    time: str
    timezone: str
    units: Units

def parse_weather_data(data):
    temp = ValueModel(data['current_weather']['temperature'], data['current_weather_units']['temperature'])
    windspeed = ValueModel(data['current_weather']['windspeed'], data['current_weather_units']['windspeed'])
    winddirection = ValueModel(data['current_weather']['winddirection'], data['current_weather_units']['winddirection'])
    
    units = Units(
        windspeed=data['current_weather_units']['windspeed'],
        winddirection=data['current_weather_units']['winddirection']
    )

    return WeatherData(
        temp=temp,
        windspeed=windspeed,
        winddirection=winddirection,
        time=data['current_weather']['time'],
        timezone=data['timezone'],
        units=units
    )
