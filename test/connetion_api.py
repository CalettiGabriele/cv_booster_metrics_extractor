import requests

data = {"path": "./test/GabrieleCaletti.pdf"}
response = requests.post("http://127.0.0.1:8000/", json=data)
print(response.json())
