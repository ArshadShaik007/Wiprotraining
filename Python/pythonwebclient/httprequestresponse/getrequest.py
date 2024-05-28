import requests

r = requests.get('https://videogamedb.uk:443/api/v2/videogame/3')

print(r.json())
