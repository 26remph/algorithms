from sys import stdin
from typing import LiteralString

import requests

host = input()
user_id = input()
keys = [tuple(key.strip().split('=')) for key in stdin]

data = dict(keys)
url = f'http://{host}/users/{user_id}'
requests.put(url, json=data)
