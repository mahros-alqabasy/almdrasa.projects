# Created by Mahros



import aiohttp
import src.utils.api as api

class Coordinate:
  def __init__(self, lati: float, long: float):
      self.lati = lati if isinstance(lati, float) else 0.0
      self.long = long if isinstance(long, float) else 0.0

  def get(self):
      return (self.lati, self.long)

  def display(self):
      print(self.get())

class Location:
  __api = api.API("https://nominatim.openstreetmap.org/")

  def __init__(self):
    pass
  
  async def getCoordinates(self, location: str = "cairo"):
    params = {
      "q": location,        
      "format": "json",     
      "limit": 1
    }

    # Await the result of the asynchronous get request
    coordinates = await self.__api.get("/search", params=params)
    
    if coordinates:
      latitude = float(coordinates[0]['lat'])
      longitude = float(coordinates[0]['lon'])
      return Coordinate(latitude, longitude)
    else:
      return None
