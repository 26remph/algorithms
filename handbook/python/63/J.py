import requests

host, user_id = [input() for _ in range(2)]
url = f'https://{host}/users/{user_id}'
requests.delete(url)
