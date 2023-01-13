import requests

res = requests.get("https://www.google.com/")
print(res.status_code)
print(res.headers)
print(res.content)
