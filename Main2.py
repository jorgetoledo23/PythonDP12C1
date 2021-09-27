import Menu
from Clases import *

mP = Menu.MenuPrincipal()

listaAutos = []
listaMecanicos = []
listaReparaciones = []

def insertarDatosTesting():
    A = Auto('GHFG23','GTSFDRSF343434','ROJO', 'KIA','RIO 5', 2013)
    A2 = Auto('WESD17','HSTDGDRSF34332','BLANCO', 'NISSAN','TERRANO', 2010)
    A3 = Auto('HTDG22','IKYUHHFTDG2323','GRIS', 'MAZDA','CX 5', 2020)
    listaAutos.append(A)
    listaAutos.append(A2)
    listaAutos.append(A3)

    M = Mecanico('1.123.123-1','ALEXIS', 'SANCHEZ', 35, 'CURICO')
    M2 = Mecanico('2.123.123-1','ARTURO', 'VIDAL', 30, 'MOLINA')
    M3 = Mecanico('3.123.123-1','GARY', 'MEDEL', 40, 'TENO')
    listaMecanicos.append(M)
    listaMecanicos.append(M2)
    listaMecanicos.append(M3)

insertarDatosTesting()

while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))

    if (oP == "3"):
        #Reparaciones ADD
        #len(listaAutos) #1,2,10,100
        if ((len(listaAutos) > 0) & (len(listaMecanicos) > 0)):
            
            mP.LimpiarConsola()

            cod = 1
            for M in listaMecanicos:
                print(f"Opcion {cod}: {M.getInfo()}")
                cod += 1
            opcion = int(input("Seleccione Opcion Mecanico Asignado a la Reparacion: "))
            mecSeleccionado = listaMecanicos[opcion - 1]

            cod = 1
            for A in listaAutos:
                print(f"Opcion {cod}: {A.getInfo()}")
                cod += 1
            opcion = int(input("Seleccione Opcion Auto Asignado a la Reparacion: "))
            autoSeleccionado = listaAutos[opcion - 1]

            valor = input("Ingrese Costo de la Reparacion: ")
            Rep = Reparacion(autoSeleccionado, mecSeleccionado, valor)
            listaReparaciones.append(Rep)
            mP.ConfirmacionIngreso('Reparacion')
        else:
            print("Error! Debe existir al menos UN (1) Auto/MEcanico para agregar Rapraciones")        


    if (oP == "7"):
        #Editar Auto
        mP.LimpiarConsola()
        cod = 1
        for A in listaAutos:
            print(f"Opcion {cod}: {A.getInfo()}")
            cod += 1
        opcion = int(input("Seleccione el Auto que desea Modificar: "))

        pat = str(input("Ingrese Patente: "))
        nchas = str(input("Ingrese Numero Chasis: "))
        col = str(input("Ingrese Color: "))
        marca = str(input("Ingrese Marca: "))
        modelo = str(input("Ingrese Modelo: "))
        year = str(input("Ingrese Año: "))

        A = Auto(pat, nchas, col, marca, year, modelo)
        listaAutos[opcion - 1] = A

        mP.ConfirmacionEdit('Auto')



    if (oP == "8"):
        #Eliminar Auto
        mP.LimpiarConsola()
        cod = 1
        for A in listaAutos:
            print(f"Opcion {cod}: {A.getInfo()}")
            cod += 1
        opcion = int(input("Seleccione el Auto que desea Eliminar: "))

        listaAutos.remove(listaAutos[opcion - 1])
        mP.ConfirmacionDelete('Auto')


    if (oP == "1"):
        #Logica para Agregar Autos
        mP.LimpiarConsola()

        print("-------------Opcion Seleccionada: Ingreso de Auto----------------")
        print(" ")

        pat = str(input("Ingrese Patente: "))
        nchas = str(input("Ingrese Numero Chasis: "))
        col = str(input("Ingrese Color: "))
        marca = str(input("Ingrese Marca: "))
        modelo = str(input("Ingrese Modelo: "))
        year = str(input("Ingrese Año: "))

        A = Auto(pat, nchas, col, marca, year, modelo)
        listaAutos.append(A)

        mP.ConfirmacionIngreso('Auto')
    
    if (oP == "4"):
        #Mostrar los Autos
        mP.LimpiarConsola()
        for A in listaAutos:
            print(A.getInfo())
        print(" ")
        input("Presione una tecla para volver al Menu Principal:")

    if (oP == "6"):
        #Mostrar las Reparaciones
        mP.LimpiarConsola()
        for R in listaReparaciones:
            print(R.getInfo())
        print(" ")
        input("Presione una tecla para volver al Menu Principal:")

    if (oP == "2"):
        mP.LimpiarConsola()
        print("-------------Opcion Seleccionada: Ingreso de Mecanico----------------")
        print(" ")
        rut = input("Ingrese Rut: ")    
        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        edad = int(input("Ingrese Edad: "))
        dir = input("Ingrese Direccion: ")           

        M = Mecanico(rut,nom,ape,edad,dir)
        listaMecanicos.append(M)

        mP.ConfirmacionIngreso('Mecanico')

    if (oP == "5"):
        #Mostrar los Mecs
        mP.LimpiarConsola()
        for M in listaMecanicos:
            print(M.getInfo())
        print(" ")
        input("Presione una tecla para volver al Menu Principal:")
