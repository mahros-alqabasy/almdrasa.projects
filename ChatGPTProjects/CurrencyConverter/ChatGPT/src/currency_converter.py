from src.utils import api
from dataclasses import dataclass

@dataclass
class StatusMessage:
    success: bool
    msg: str = None
    data: object = None

class CurrencyConverter(api.API):
    def __init__(self):
        super().__init__()

        self.currencies = None

    def getCurrencies(self):
        response = self.get("/list")
        if response["success"]:
            self.currencies = response["currencies"]
            return StatusMessage(success=True, data=self.currencies)
        return StatusMessage(success=False, msg=response.get("message", "Unknown error"))

    def showCurrencies(self):
        if self.currencies:
            print(", ".join(sorted(self.currencies.keys())))

    def convert(self, base: str, amount: float, to: str):
        while self.currencies is None:
            self.getCurrencies()

        if base not in self.currencies:
            return StatusMessage(success=False, msg=f"{base} is not a valid currency")

        if to not in self.currencies:
            return StatusMessage(success=False, msg=f"{to} is not a valid currency")

        if amount <= 0:
            return StatusMessage(success=True, data=0.0)

        response = self.get("/convert", params={
            "to": to,
            "from": base,
            "amount": amount
        })

        if response.get("success"):
            return StatusMessage(success=True, data=response["result"])

        return StatusMessage(success=False, msg=response.get("error", {}).get("info", "Unknown error"))
