import requests

# send query parameters as dictionary variables

response = requests.get('https://aqi.github.com/search/repositories',
                        params=("language:python", "stars", "desc"))

json_response = response.json()

print(json_response)
