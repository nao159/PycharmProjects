import requests
from pprint import pprint


url = 'https://api.npoint.io/43644ec4f0013682fc0d'
request = requests.get(url=url)
data = request.json()

pprint(data)