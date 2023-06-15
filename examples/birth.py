from ghostpip import submit_birth_information

def test_submit_birth_information():
    api_key = "myapikey"
    birth_information = "Birth details"
    date_of_birth = "2000-01-01"

    response = submit_birth_information(api_key, birth_information, date_of_birth)

    print(response)

test_submit_birth_information()
