import requests


class DataManager:
    def __init__(self):
        self.api_endpoint = "https://api.sheety.co/d1cf2df178040bfec9803127c861cb7e/flightDeals/prices"
        self.response = requests.get(url=self.api_endpoint)
        self.data = (self.response.json())['prices']

    def update_codes(self, data):
        for city in data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.api_endpoint}/{city['id']}",
                json=new_data
            )


def callBack(temp):
    if temp in temp:
        print(f"There is new temperature recorded in the  {temp}")
    return True
