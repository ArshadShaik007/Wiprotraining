import grequests

reqs = []

for ship_id in range(0, 50):
    reqs.append(grequests.get(f'https://swapi.dev/api/starships/{ship_id}'))

for r in grequests.map(reqs):
    print(r.json())
