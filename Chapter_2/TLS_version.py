import requests
print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()["tls_version"])
