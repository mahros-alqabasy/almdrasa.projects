# Created by Mahros

# Dependencies
import requests

class API:
  def __init__(self, url:str="https://api.apilayer.com/currency_data", apikey:str="PEGg8fJRDDCW1yH4o8dm9uMT2Aur61dB"):
    self.url      = url
    self.headers  = {
      "apikey":apikey
    }

  def concate_urls(self, *urls):
    segments = [*urls]

    return "/".join([url.strip("/") for url in segments])


  def get(self, endpoint, params=None):
    url = self.concate_urls(self.url, endpoint)
    print(url)
    response = requests.get(url, headers=self.headers, params=params)

    return response.json()
    
  def post(self, endpoint, data=None):
    url = self.concate_urls(self.url, endpoint)
    response = requests.post(url, headers=self.headers, json=data)

    return response.json()
