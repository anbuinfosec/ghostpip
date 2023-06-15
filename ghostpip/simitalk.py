import requests
import json

def simulate_talk(api_key, question, language_code):
    url = 'https://ghost.toxinum.xyz/api/v1/simitalk'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'apiKey': api_key,
        'ask': question,
        'lc': language_code
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text
