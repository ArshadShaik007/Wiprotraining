import requests

r = requests.get("https://videogamedb.uk:443/api/v2/videogame")

# fetch the json format of the response

print(r.json())

# text
print(r.text)

# status code
print(r.status_code)

# response url
print(r.url)

# request object
print(r.request)

# check encoding of the response
print(r.encoding)

# check history
print(r.history)

# check headers
print(r.headers)

# check header values
print(r.headers["Content-type"])
# close the connecetion
r.close()

