import requests


schema = "http://"
url = schema + input()

response = requests.get(url).json()
print(sum(x for x in response if isinstance(x, int)))
