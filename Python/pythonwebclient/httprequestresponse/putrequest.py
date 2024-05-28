import requests

data ={
  "category": "Platform",
  "name": "Donkey Kong",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85
}
r = requests.put('https://videogamedb.uk:443/api/v2/videogame/1',json=data)

print(r.json())
