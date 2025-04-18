#!/usr/bin/python3
# /src/scrapper.py
# Created by Mahros



# Dependencies
import requests
from bs4 import BeautifulSoup

# Imports
from src.utils import logger as log
from src.utils import url as url
# _name: means that this is an attibute not function
# name: means that this is a function not attibute

# Scrapper
class Scrapper:
  logger = log.Logger()
  def __init__(self, url:str="google.com", verbose:bool=False):
    self.url = url.strip()
    self.verbose = verbose

  # request
  def request(self, route:str="/"):
    if self.verbose:
      self.logger.log("Requesting data from site...")
      
    headers = {'User-Agent': 'Mozilla/5.0'}
    return requests.get(url.Url.join(self.url, route), headers).text
  
  
  # scrap
  def scrap(self, response:str):
    if self.verbose:
      self.logger.log("Beautifing Responses....")
    
    return BeautifulSoup(response, "html.parser") 

# test - only work if you run this file only eg. python /src/scrapper.py
if __name__ == "__main__":
  try:
    THNScrapper = Scrapper(url="https://almdrasa.com/")
    THNScrapper.scrap("/")
  except Exception as Error:
    print(Error)
    
