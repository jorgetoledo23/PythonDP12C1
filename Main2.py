import Menu
from Clases import *

mP = Menu.MenuPrincipal()

listaAutos = []
listaMecanicos = []
listaReparaciones = []

while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(":"))

    if (oP == "1"):
        #Logica para Agregar Autos
        mP.LimpiarConsola()
        pat = str(input("Ingrese Patente: "))
        nchas = str(input("Ingrese Numero Chasis: "))
        col = str(input("Ingrese Color: "))
        marca = str(input("Ingrese Marca: "))
        modelo = str(input("Ingrese Modelo: "))
        year = str(input("Ingrese Año: "))

        A = Auto(pat, nchas, col, marca, year, modelo)
        listaAutos.append(A)
    
    if (oP == "4"):
        #Mostrar los Autos
        for A in listaAutos:
            print(A.getInfo())
        input("Presione una tecla para volver al Menu Principal:")

    if (oP == "2"):
        mP.LimpiarConsola()
        rut = input("Ingrese Rut: ")    
        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        edad = int(input("Ingrese Edad: "))
        dir = input("Ingrese Direccion: ")           

        M = Mecanico(rut,nom,ape,edad,dir)
        listaMecanicos.append(M)


    if (oP == "5"):
        #Mostrar los Autos
        for M in listaMecanicos:
            print(M.getInfo())
        input("Presione una tecla para volver al Menu Principal:")
