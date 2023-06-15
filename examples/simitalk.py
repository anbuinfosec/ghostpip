from ghostpip import simulate_talk

def test_simulate_talk():
    api_key = "myapikey"
    question = "How are you?"
    language_code = "en"

    response = simulate_talk(api_key, question, language_code)

    
    print(response)

test_simulate_talk()
