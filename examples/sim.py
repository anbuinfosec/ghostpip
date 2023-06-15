from ghostpip import get_sim_info

def test_get_sim_info():
    api_key = "myapikey"
    phone_number = "0123456789"

    response = get_sim_info(api_key, phone_number)

    print(response)

test_get_sim_info()
