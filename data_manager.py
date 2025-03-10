import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(SHEETY_ENDPOINT, auth=self._authorization)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, auth=self._authorization)
            print(response.text)
