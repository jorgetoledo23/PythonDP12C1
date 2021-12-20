import requests

peticionHTTP = requests.get('https://catfact.ninja/fact')


dato = peticionHTTP.json()

print(dato['fact'])

