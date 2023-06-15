import requests
import json

def signin(email, password):
    url = 'https://ghost.toxinum.xyz/api/v1/signin'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'email': email,
        'password': password
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text
