from flight_search import FlightSearch
from data_manager import DataManager


flight_search = FlightSearch()
data_manager = DataManager()

for city in data_manager.data:
    if city['iataCode'] == '':
        city['iataCode'] = flight_search.get_code(city['city'])
    else:
        break
data_manager.update_codes(data_manager.data)

for city in data_manager.data:
    flight_search.search_flights(city['iataCode'], city['lowestPrice'])

