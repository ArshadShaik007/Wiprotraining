import http.client
import logging

# configure the logging

logging.basicConfig(filename = "httpclienterrors.log", level = logging.ERROR)
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
    logging.error("an error occured")
finally:
    conn.close()
