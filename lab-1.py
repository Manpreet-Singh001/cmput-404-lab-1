import requests

#res = requests.get("https://www.google.com/")
#print(res.status_code)
#print(res.headers)
#print(res.content)


res = requests.get("https://raw.githubusercontent.com/Manpreet-Singh001/cmput-404-lab-1/main/lab-1.py")
print(res.content)
