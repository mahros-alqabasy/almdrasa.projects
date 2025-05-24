# src/weather_app.py

import tkinter as tk
import asyncio
from src import gui
from src.utils.api import API
from src.components.body import Body
from src.utils.location import Location
from src.components.tool_bar import ToolBar
from src.components.status_bar import StatusBar
from src.utils import weather_data as wd

class WeatherApp(gui.Gui):
    api = API("https://api.open-meteo.com/v1/forecast")
    
    def __init__(self):
        conf = gui.AppConf(
            window=gui.WindowConf(
                title="Weather App",
                size=(800, 600)
            )
        )
        super().__init__(conf)

        # components
        self.body = Body(self.root, self.loadData)
        self.tool_bar = ToolBar(self.root)
        self.status_bar = StatusBar(self.root)

        self.init_widgets()

    async def loadData(self, location: str):
        coordinates = await Location().getCoordinates(location)

        if coordinates:
            params = {
                "latitude": coordinates.lati,
                "longitude": coordinates.long,
                "current_weather": "true"
            }

            response = await self.api.get("/", params=params)

            if response:
                weather_data = wd.parse_weather_data(response)
                self.display_weather_data(weather_data)
                return weather_data  # ✅ return it
            else:
                print("No weather data found.")
                return None
        else:
            print("Invalid coordinates.")
            return None

    def display_weather_data(self, weather_data):
        # Pass the weather data to the Body component for display
        self.body.update_weather_info(weather_data)

    def init_widgets(self):
        # widgets
        self.tool_bar.pack(side="top", fill="x")
        self.body.pack(side="top", fill=tk.BOTH, expand=True)
        self.status_bar.pack(side="bottom", fill="x")
