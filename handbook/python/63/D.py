import requests


schema = "http://"
url = schema + input()
require_key = input()

response = requests.get(url).json()
print(response.get(require_key, 'No data'))