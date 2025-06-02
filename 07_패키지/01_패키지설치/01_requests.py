import requests

res = requests.get("https://알클.com")
print(res.status_code)
print(res.text)