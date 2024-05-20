from data_manager import DataManager
from flight_search import FlightSearch

# Getting data from data manager and storing it in sheet_data
data_manager = DataManager()
sheet_data = data_manager.get_sheety_data()

# Flight search instance
flight_search = FlightSearch()

# Checking if sheet_data contains any value for iata codes
for data in sheet_data:
    if data['iataCode'] == "":
        data['iataCode'] = flight_search.get_destination_code()

# Updating sheety_data
data_manager.destination_data = sheet_data
data_manager.update_destination_code()