import requests

data = {
  "category": "Platform",
  "name": "Mario",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85
}

r = requests.post('https://videogamedb.uk:443/api/v2/videogame', json=data)

print(r.json())
