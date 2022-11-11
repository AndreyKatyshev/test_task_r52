from pprint import pprint

import requests

response = requests.get('https://swapi.dev/api/starships/9/')
characters = response.json().get('results')
print(response.text)