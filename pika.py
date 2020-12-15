import pprint
import requests


r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pprint.pprint(r.json())
