from ghostpip import get_device_info

def test_get_device_info():
    api_key = "myapikey"
    phone_number = "0123456789"

    response = get_device_info(api_key, phone_number)
    print(response)

test_get_device_info()
