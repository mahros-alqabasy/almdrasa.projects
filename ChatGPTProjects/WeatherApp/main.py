# Created by Mahros


# dependencies
from src import gui
import tkinter as tk 
import src.weather_app as wa
import src.utils.api as api

def main():
  
  # app
  app = wa.WeatherApp()

  # show
  app.run()


# run
if __name__ == "__main__":
  main()
