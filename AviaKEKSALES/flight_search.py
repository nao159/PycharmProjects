import requests
import datetime as dt
from datetime import timedelta
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "j4oZKr8siz3umpA_OJYBC0KOmuxtM6VY"


class FlightSearch:

    def __init__(self):
        self.my_city_code = "LED",
        self.my_city_name = "Saint-Petersburg"

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query, auth=("Nao", "031099maW"))
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_prices(self, data):
        price_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {'apikey': TEQUILA_API_KEY}
        now = dt.datetime.now()
        conv_now = now.strftime("%d/%m/%Y")
        end_day = now + timedelta(days=180)
        conv_end_day = end_day.strftime("%d/%m/%Y")
        json_query = {
            'fly_from': self.my_city_code,
            'fly_to': data['iataCode'],
            'date_from': conv_now,
            'date_to': conv_end_day,
            'adults': 1,
            'curr': "RUB",
            'price_to': data['lowestPrice'],
            'sort': 'date',
            'limit': 1
        }

        response = requests.get(url=price_endpoint, params=json_query, headers=headers, auth=("Nao", "031099maW"))
        converted_Data = response.json()
        print(f"You can fly from {self.my_city_name} to {data['city']} in {converted_Data['data'][0]['local_departure']} with price of {converted_Data['data'][0]['price']}")



