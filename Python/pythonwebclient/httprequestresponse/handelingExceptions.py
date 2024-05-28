import http.client
try:
    conn = http.client.HTTPSConnection("https://videogamedb.uk")
    conn.request("GET", "/api/videogame/")
    response= conn.getresponse()

    # check the status code
    if response.status ==200:
        print("request successfull")
    elif response.status ==404:
        print("Resorce not found")
    else:
        print("Unexpected status code:", response.status)
except http.client.HTTPException as e:
    print("Http exception",e)
except Exception as e:
    print("an error occured")
