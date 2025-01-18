import requests

host = input()
data = {
    "username": input(),
    "last_name": input(),
    "first_name": input(),
    "email": input()
}
url = f'http://{host}/users'
requests.post(url, json=data)

