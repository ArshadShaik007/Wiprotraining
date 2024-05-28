import httpx

data = {'name': 'john kennedy'}

r = httpx.post('https://httpbin.org/post',data=data)

print(r.json())