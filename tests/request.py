import requests
import json


def send_get():
    url = "http://192.168.1.224:9933"
    params = {
        "Content-Type": "application/json"
    }

    message = {"jsonrpc": "2.0", "method": "system_name", "params": [], "id": 1}
    print(json.dumps(message))

    r = requests.get(url=url, json=json.dumps(message), params=params)

    print(str(r.content))


def send_post():
    url = "http://192.168.1.224:9933"
    params = {
        "Content-Type": "application/json"
    }

    message = {"jsonrpc": "2.0", "method": "system_name", "params": [], "id": 1}
    print(json.dumps(message))

    r = requests.post(url=url, json=message, params=params)

    print(str(r.content))


send_post()

