import requests

data = {'name': 'sam'}

r = requests.post('https://httpbin.org/post', json=data)

print(r.json())
