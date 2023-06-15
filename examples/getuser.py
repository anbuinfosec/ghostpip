from ghostpip import get_user

def test_get_user():
    api_key = "myapikey"

    response = get_user(api_key)

    print (response)

test_get_user()
