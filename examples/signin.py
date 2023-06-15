from ghostpip import signin

def test_signin():
    email = "johndoe@example.com"
    password = "mypassword"

    response = signin(email, password)

    print(response)

test_signin()
