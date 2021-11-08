from Model.Clases import *
from ConexionMySql import DAO

dao = DAO()
mP = MenuPrincipal()

while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))

    if oP == "1":
        mP.LimpiarConsola()
        mP.MenuSecundario("Cliente")
        oP = str(input(" : "))

        if oP == "1":
            #Insertar data Cliente a la Base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Cliente =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarCliente(C)

            mP.ConfirmacionIngreso("Cliente")

        if oP == "2":
            #Listar TODOS los clientes que esten almacenados en la base de datos
            mP.LimpiarConsola()
            print("======= Listando Clientes =======")
            print("=================================")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfo())

            print("")
            input("Presione Enter para Continuar...")

        if oP == "0":
            pass

    if oP == "2":
        #Gestionamos Mecanicos
        mP.LimpiarConsola()
        mP.MenuSecundario("Mecanico")
        oP = str(input(" : "))

        if oP == "1":
            #Insertar data Mecanico a la Base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Mecanico =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            M = Mecanico(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarMecanico(M)

            mP.ConfirmacionIngreso("Mecanico")

        if oP == "2":
            #Listar TODOS los Mecacnicos que esten almacenados en la base de datos
            mP.LimpiarConsola()
            print("======= Listando Mecanicos =======")
            print("=================================")
            print("")

            for M in dao.ListarMecanicos():
                print(M.getInfo())

            print("")
            input("Presione Enter para Continuar...")


        if oP == "0":
            pass