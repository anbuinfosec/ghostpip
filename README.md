# GHOSTPIP

**GHOSTPIP** is a Python module that provides convenient methods for interacting with the `ghost.toxinum.xyz` API. It enables you to perform various operations such as user signup, signin, retrieving user information, fetching location details, getting SIM information, device details, balance information, and more.

## Installation

You can install **GHOSTPIP** using pip:

```shell
pip install ghostpip
```

## Usage

```python
from ghostpip import (
    signup,
    signin,
    get_user,
    get_location,
    get_sim_info,
    get_device_info,
    get_account_balance,
    submit_birth_information,
    submit_nid_information,
    simulate_talk,
    teach_chatbot
)
```

### Function Examples

Here are some examples of how to use the functions:

#### Signup a new user:

```python
signup("John Doe", "johndoe@example.com", "password123")
```

#### Signin with an existing user:

```python
signin("johndoe@example.com", "password123")
```

#### Get user information:

```python
get_user("your-api-key")
```

#### Get location details:

```python
get_location("your-api-key", "0123456789")
```

#### Get SIM information:

```python
get_sim_info("your-api-key", "0123456789")
```

#### Get device information:

```python
get_device_info("your-api-key", "0123456789")
```

#### Get account balance:

```python
get_account_balance("your-api-key", "0123456789")
```

#### Submit birth information:

```python
submit_birth_information("your-api-key", "birth-info", "dob")
```

#### Submit NID information:

```python
submit_nid_information("your-api-key", "nid-info", "dob")
```

#### Simulate talk:

```python
simulate_talk("your-api-key", "ask", "lc")
```

#### Teach chatbot:

```python
teach_chatbot("your-api-key", "ask", "ans", "lc")
```


## API Documentation

For detailed information on the API endpoints and parameters, please refer to the [ghost.toxinum.xyz API documentation](https://ghost.toxinum.xyz/docs.html).

## Contributing

Contributions to **GHOSTPIP** are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request on the GitHub repository.

## Contact

- Facebook: [Mohammad Alamin](https://www.facebook.com/Illusionghost?mibextid=ZbWKwL)
- Telegram: [XYRUS INC](https://t.me/xyrusinc)
- GitHub: [@illusionghost3](https://github.com/illusionghost3)

### Thanks For Star🙏👨‍💻

[![Stargazers repo](https://reporoster.com/stars/illusionghost3/ghostpip)](https://github.com/illusionghost3/ghostpip/stargazers)

### Thanks For Fork 🙏👨‍💻

[![Forkers repo](https://reporoster.com/forks/illusionghost3/ghostpip)](https://github.com/illusionghost3/ghostpip/network/members)

## License

This project is licensed under the [MIT License](LICENSE).
