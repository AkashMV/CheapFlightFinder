import requests
from datetime import datetime, timedelta
from notif_manager import SendMessage

class FlightSearch:
    def __init__(self):
        self.api_endpoint = "https://tequila-api.kiwi.com"
        self.api_key = "t3sCRyEPOHR5OL2JkvlxHvHAxy0ypF0w"
        self.location = 'LON'
        self.date_now = datetime.now() + timedelta(days=1)
        self.date = self.date_now.strftime("%d/%m/%Y")
        self.date_after_six_months = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")
        self.send_message = SendMessage()

    def search_flights(self, final_location, max_price):
        params = {
            'fly_from': self.location,
            'fly_to': final_location,
            'date_from': self.date,
            'date_to': self.date_after_six_months,
            "price_from": 0,
            "price_to": max_price,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        header = {
            'apikey': self.api_key,
        }
        response = requests.get(url=f"{self.api_endpoint}/v2/search", params=params, headers=header)
        data = response.json()
        if len(data["data"]) > 0:
            flight_details = data['data'][0]
            price = flight_details['price']
            city = flight_details['cityFrom']
            city_code = flight_details['cityCodeFrom']
            dest_city = flight_details['cityTo']
            dest_city_code = flight_details['cityCodeTo']
            arrival = flight_details['local_arrival'][0:10]
            departure = flight_details['local_departure'][0:10]
            message = f"Low Price Alert! Only {price} to fly from {city}-{city_code} to {dest_city}-{dest_city_code}, "\
                      f"{arrival} to {departure}"
            print(message)
            self.send_message.send_sms(message)
        else:
            return False

    def new_func(self, ):
        pass

    def get_code(self, city):
        location_endpoint = f"{self.api_endpoint}/locations/query"
        headers = {"apikey": self.api_key}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()
        code = results['locations'][0]['code']
        return code
