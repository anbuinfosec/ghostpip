import requests
import json

def teach_chatbot(api_key, question, answer, language_code):
    url = 'https://ghost.toxinum.xyz/api/v1/simiteach'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'apiKey': api_key,
        'ask': question,
        'ans': answer,
        'lc': language_code
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text
