import requests

url = "https://jsonplaceholder.typicode.com/posts"
session = requests.Session()

#Make the first request

response = session.get(url)

print(response.json())

#Make another request

response = session.post(url, json={"title": "New Post", "body": "Content"})
print(response.json())

#Close the session

session.close()