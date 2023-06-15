import requests
import json

def submit_birth_information(api_key, birth_information, date_of_birth):
    url = 'https://ghost.toxinum.xyz/api/v1/birth'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'apiKey': api_key,
        'birth': birth_information,
        'dob': date_of_birth
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text