# Created by Mahros



# Dependencies
import requests
import aiohttp


class API:
  def __init__(self, url:str="https://api.apilayer.com/currency_data", apikey:str="PEGg8fJRDDCW1yH4o8dm9uMT2Aur61dB"):
    self.url      = url
    self.headers  = {
      "apikey":apikey,
       "User-Agent": "MyWeatherApp/1.0 (contact@example.com)"
    }

  def concate_urls(self, *urls):
    segments = [*urls]

    return "/".join([url.strip("/") for url in segments])


  async def get(self, endpoint, params=None):
    url = self.concate_urls(self.url, endpoint)
    async with aiohttp.ClientSession() as session:
      async with session.get(url, headers=self.headers, params=params) as response:
        if response.status == 200:
          return await response.json()
        else:
            return {}

  async def post(self, endpoint, data=None):
    url = self.concate_urls(self.url, endpoint)
    async with aiohttp.ClientSession() as session:
      async with session.post(url, headers=self.headers, json=data) as response:
        return await response.json()
