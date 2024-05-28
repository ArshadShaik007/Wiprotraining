import requests

# send query parameters as dictionary variables

response = requests.get('https://api.github.com/search/repositories',
                        params={"q": "language:python", "sort": "stars", "order": "desc"})

json_response = response.json()

print(json_response)

response = requests.get('https://reqres.in/api/users?page=2')

print(response.json())
