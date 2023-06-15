from ghostpip import get_location

def test_get_location():
    api_key = "myapikey"
    phone_number = "019XXXXXXXX"

    response = get_location(api_key, phone_number)

    print(response)

test_get_location()
