import requests
from pprint import pprint

PASSWORD = 'p4cGdrHv4@xptkw'
API_KEY = '56582d71e9838a5ec7a1482258e74986'
LINK = f'https://api.themoviedb.org/3/search/movie?'
movie = 'Eternity'

request = requests.get(url=LINK, params={'api_key': API_KEY, 'query': movie})
data = request.json()['results']
pprint(data)
