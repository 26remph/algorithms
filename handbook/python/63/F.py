import requests


host = input()
url = f"http://{host}/users"

response = requests.get(url).json()
ans = sorted(response, key=lambda x: (x["last_name"], x["first_name"]))
for user in ans:
    print(user["last_name"], user["first_name"])
