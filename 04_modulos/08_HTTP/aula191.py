# requests para requisições HTTP
# pip install requests types-requests
# Requests é uma biblioteca Python para fazer requisições HTTP de forma simples e intuitiva.
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)