import requests

def MostrarMenu():

    print("[1] Obtener Dato de Gato ")
    print("[2] Obtener Todos los Datos de Gato ")
    print("[3] Eliminar Dato de Gato ")

MostrarMenu()

opcion = input("Seleccione una Opcion: ")

if opcion == "1":
    peticionHTTP = requests.get('https://catfact.ninja/fact')
    dato = peticionHTTP.json()
    #Alamcenar dato en MI base de datos
    hecho = dato['fact']
    largoDato = dato['length']

    print(hecho)
    print(largoDato)

