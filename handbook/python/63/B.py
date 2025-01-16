import requests


schema = "http://"
url = schema + input()
answer = 0
while (data := int(requests.get(url).text)) != 0:
    answer += data

print(answer)
