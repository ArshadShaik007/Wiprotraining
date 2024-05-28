import http.client
import circuitbreaker

@circuitbreaker.circuit
def make_request():
    conn = http.client.HTTPSConnection("https://videogamedb.uk")
    conn.request("GET", "/api/videogame/")
    response = conn.getresponse()
    conn.close()
    # check the status code
    if response.status == 200:
        print("request succesfull")
    else:
        raise Exception("Request failed withtatus code",response.status)

    try:
        result = make_request()
        print(result)
    except circuitbreaker.CircuitBreakerError as e:
        print("Circuit Breaker is open request not sent")
