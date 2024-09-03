import requests

HELLO_MICROSERVICE_URL = "http://127.0.0.1:54255/hello" #change according to url given by kubernetes
WORLD_MICROSERVICE_URL = "http://127.0.0.1:54265/world" #change according to url given by kubernetes

def call_hello():
    try:
        response = requests.get(HELLO_MICROSERVICE_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error calling hello microservice: {e}")
        return ""

def call_world():
    try:
        response = requests.get(WORLD_MICROSERVICE_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error calling world microservice: {e}")
        return ""

if __name__ == "__main__":
    hello_response = call_hello()
    world_response = call_world()

    if hello_response and world_response:
        print(f"{hello_response} {world_response}")
    else:
        print("Failed to get response from microservices.")