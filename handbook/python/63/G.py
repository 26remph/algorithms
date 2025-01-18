from sys import stdin

import requests

host, user_id = [input() for _ in range(2)]
letter = "".join(s for s in stdin)

response = requests.get(f"http://{host}/users/{user_id}")
if response.status_code == 200:
    response = response.json()
    print(letter.format(**response))
else:
    print('Пользователь не найден')
