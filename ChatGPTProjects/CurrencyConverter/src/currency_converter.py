# Created by Mahros


# imports
from src.utils import api
from dataclasses import dataclass

@dataclass
class StatusMessage:
  success:bool
  msg:str=None
  data:object=None

class CurrencyConverter(api.API):
  _currencies = None
  def __init__(self):
    super().__init__(url="https://api.apilayer.com/currency_data", apikey="PEGg8fJRDDCW1yH4o8dm9uMT2Aur61dB")
    self.getCurrencies()
  
  def getCurrencies(self):
    response = self.get("/list")
    if response["success"]:
      self._currencies = response["currencies"] 
      return StatusMessage(success=True, data=self._currencies)
    return StatusMessage(success=False, msg=response["message"])

  def convert(self, base:str, amount:float, to:str):
    while self._currencies == None:
      self.getCurrencies()
    
    if base not in self._currencies:
      return StatusMessage(success=False, msg=f"{base} is not valid currency")
      
    if to not in self._currencies:
      return StatusMessage(success=False, msg=f"{to} is not valid currency")
      


    if amount <= 0:
      return StatusMessage(success=True, data=0.0)
    
    response = self.get("/convert", params={
      "to":to,
      "from":base,
      "amount":amount
    })

    if response["success"]:
      return StatusMessage(success=True, data=response["result"])
    
    return StatusMessage(sucess=False,msg=response["error"]["info"])
    
