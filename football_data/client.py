import os
import requests
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class APIClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("FOOTBALL_DATA_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Please set FOOTBALL_DATA_API_KEY environment variable or pass it to the client.")
        self.base_url = "https://api.football-data.org/v4/"
        self.headers = {"X-Auth-Token": self.api_key}

    def _request(self, method: str, endpoint: str, params: Optional[dict] = None) -> dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            # TODO: Add more specific error handling for 4xx and 5xx errors
            print(f"HTTP error occurred: {err}")
            raise
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
            raise

    def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        return self._request("GET", endpoint, params)
