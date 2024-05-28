import requests

r = requests.delete('https://videogamedb.uk:443/api/v2/videogame/1')

print(r.text)
