from sys import stdin

import requests


schema = "http://"
url = schema + input()

paths = [p.strip() for p in stdin]

ans = 0
for path in paths:
    lst = requests.get(url + path).json()
    ans += sum(lst)

print(ans)
