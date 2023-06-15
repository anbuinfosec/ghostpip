from ghostpip import signup

def test_signup():
    name = "John Doe"
    email = "johndoe@example.com"
    password = "mypassword"

    response = signup(name, email, password)

    print(response)

test_signup()
