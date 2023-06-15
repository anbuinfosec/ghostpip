from ghostpip import teach_chatbot

def test_teach_chatbot():
    api_key = "myapikey"
    question = "What is the capital of France?"
    answer = "The capital of France is Paris."
    language_code = "en"

    response = teach_chatbot(api_key, question, answer, language_code)

    print(response)

test_teach_chatbot()
