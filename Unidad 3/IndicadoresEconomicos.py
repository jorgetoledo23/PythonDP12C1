import builtins
import requests

r = requests.get("https://mindicador.cl/api")

dato = r.json()

uf = dato['uf']
valorUf = uf['valor']
print(f"Valor actual de la UF: {valorUf}")


bitcoin = dato['bitcoin']
valorBitcoin = bitcoin['valor']

print(f"Valor actual del Bitcoin: {valorBitcoin}")

