import json
import urllib3

data = {'name': 'john kennedy'}

http = urllib3.PoolManager()

encoded_data = json.dumps(data).encode('utf-8')

r = http.request(
    'POST',
    'https://httpbin.org/post',
    body=encoded_data,
    headers={}

)
