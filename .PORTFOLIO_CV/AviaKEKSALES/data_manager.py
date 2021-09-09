import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/de32964600e1ab52d3838a34e73d0edd/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=("Nao", "031099maW"))
            print(response.status_code)
            data = response.json()
            self.destination_data = data["prices"]
            return self.destination_data
        except KeyError:
            print("unexpected behaviour. Please check your token at tequilla kiwi")
        finally:
            raise KeyError("check your API token")



    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=("Nao", "031099maW")
            )
            print(response.text)