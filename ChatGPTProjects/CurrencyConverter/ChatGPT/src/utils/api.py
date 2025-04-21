import requests
import os
from dotenv import load_dotenv

load_dotenv()

class API:
    def __init__(self, url: str = "https://api.apilayer.com/currency_data", apikey: str = None):
        self.url = url
        self.headers = {
            "apikey": apikey or os.getenv("API_KEY")
        }

    def concate_urls(self, *urls):
        return "/".join(url.strip("/") for url in urls)

    def get(self, endpoint, params=None):
        url = self.concate_urls(self.url, endpoint)
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"success": False, "message": str(e)}

    def post(self, endpoint, data=None):
        url = self.concate_urls(self.url, endpoint)
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"success": False, "message": str(e)}
