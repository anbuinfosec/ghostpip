import requests
import json

def getuser(api_key):
    url = 'https://ghost.toxinum.xyz/api/v1/getuser'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'apiKey': api_key
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text