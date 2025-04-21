# src/components/body.py

import tkinter as tk
import asyncio

class Body(tk.Frame):
    def __init__(self, parent, onSearchClicked):
        super().__init__(parent, bd=1, bg="lightblue")
        self.onSearchClicked = onSearchClicked
        self.init()

    def init(self):
        self.weather_labels = []

        # Search bar
        self.search_label = tk.Label(self, text="Enter location:")
        self.search_label.pack(side="top", fill="x")

        self.location_entry = tk.Entry(self)
        self.location_entry.pack(side="top", fill="x")

        self.search_button = tk.Button(self, text="Search", command=self.search_weather)
        self.search_button.pack(side="top", fill="x")

    async def search_weather(self):
        location = self.location_entry.get()
        if location:
            # Trigger the loadData method in the WeatherApp with the location
            result = await self.onSearchClicked(location)
            
            self.update_weather_info(result)

    def update_weather_info(self, weather_data):
        for label in self.weather_labels:
            label.destroy()


        # Create and pack the new labels for weather data
        self.weather_labels.append(tk.Label(self, text=f"Temperature: {weather_data.temp.value} {weather_data.temp.unit}"))
        self.weather_labels[-1].pack(side="top", fill="x")

        self.weather_labels.append(tk.Label(self, text=f"Windspeed: {weather_data.windspeed.value} {weather_data.windspeed.unit}"))
        self.weather_labels[-1].pack(side="top", fill="x")

        self.weather_labels.append(tk.Label(self, text=f"Wind Direction: {weather_data.winddirection.value} {weather_data.winddirection.unit}"))
        self.weather_labels[-1].pack(side="top", fill="x")

        self.weather_labels.append(tk.Label(self, text=f"Time: {weather_data.time}"))
        self.weather_labels[-1].pack(side="top", fill="x")

        self.weather_labels.append(tk.Label(self, text=f"Timezone: {weather_data.timezone}"))
        self.weather_labels[-1].pack(side="top", fill="x")
