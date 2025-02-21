#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import flight_data
from flight_search import FlightSearch
import notification_manager
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iatacode(row["city"])
    print(f"sheet_data: \n{sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()