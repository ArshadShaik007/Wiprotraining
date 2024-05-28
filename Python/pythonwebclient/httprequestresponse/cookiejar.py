import http.client
import http.cookiejar

# create a cokkie jar to store cookies
cookie_jar = http.cookiejar.CookieJar

# create an http client with cookie support
conn = http.client.HTTPConnection("https://videogamedb.uk",cookies=cookie_jar)

# send request

conn.request("GET", "/")

# get response

response = conn.getresponse()