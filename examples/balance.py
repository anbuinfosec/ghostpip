from ghostpip import get_account_balance

def test_get_account_balance():
    api_key = "myapikey"
    phone_number = "0123456789"

    response = get_account_balance(api_key, phone_number)
    print(response)
test_get_account_balance()
