from ghostpip import submit_nid_information

def test_submit_nid_information():
    api_key = "myapikey"
    nid_information = "NID details"
    date_of_birth = "2000-01-01"

    response = submit_nid_information(api_key, nid_information, date_of_birth)

    print(response)

test_submit_nid_information()
