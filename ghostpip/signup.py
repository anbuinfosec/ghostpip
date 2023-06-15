import requests
import json

def signup(name, email, password):
    url = 'https://ghost.toxinum.xyz/api/v1/signup'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'name': name,
        'email': email,
        'password': password
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text
