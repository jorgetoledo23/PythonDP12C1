import mysql.connector
from mysql.connector import errorcode
from Model.Clases import *
class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='',
                host='127.0.0.1',
                database='d_n2_p12_c1')
            #
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


    def InsertarCliente(self, C):
        add_cliente = ("insert into tbl_clientes"
                        "(rut, nombres, apellidos, direccion, correo, telefono, comuna)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_cliente = (C.getRut(), C.getNombres(), C.getApellidos(), C.getDireccion(), C.getCorreo(), C.getTelefono(), C.getComuna())

        cursor = self.cnx.cursor()
        cursor.execute(add_cliente, data_cliente)
        self.cnx.commit()


    def ActualizarCliente(self, C, Rut):
        add_cliente = ("UPDATE tbl_clientes SET rut = %s, nombres = %s, apellidos = %s, correo = %s, telefono = %s, "
                    " direccion = %s, comuna = %s"
                    " WHERE rut = %s")

        data_cliente = (C.getRut(), C.getNombres(), C.getApellidos(), C.getCorreo(), C.getTelefono(), C.getDireccion(), C.getComuna(), Rut)

        cursor = self.cnx.cursor()
        cursor.execute(add_cliente, data_cliente)
        self.cnx.commit()


    def EliminarCliente(self, Rut):
        delete_cliente = ("DELETE FROM tbl_clientes WHERE rut = %s")

        data_cliente = (Rut,)

        cursor = self.cnx.cursor()
        cursor.execute(delete_cliente, data_cliente)
        self.cnx.commit()

    def EliminarMecanico(self, Rut):
        delete_mecanico = ("DELETE FROM tbl_mecanicos WHERE rut = %s")

        data_mecanico = (Rut,)

        cursor = self.cnx.cursor()
        cursor.execute(delete_mecanico, data_mecanico)
        self.cnx.commit()

    def EliminarVehiculo(self, Patente):
        delete_auto = ("DELETE FROM tbl_autos WHERE patente = %s")

        data_auto = (Patente,)

        cursor = self.cnx.cursor()
        cursor.execute(delete_auto, data_auto)
        self.cnx.commit()


    def InsertarMecanico(self, M):
        add_mecanico = ("insert into tbl_mecanicos"
                        "(rut, nombres, apellidos, direccion, correo, telefono, comuna)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_mecanico = (M.getRut(), M.getNombres(), M.getApellidos(), M.getDireccion(), M.getCorreo(), M.getTelefono(), M.getComuna())

        cursor = self.cnx.cursor()
        cursor.execute(add_mecanico, data_mecanico)
        self.cnx.commit()

    def ActualizarMecanico(self, M, Rut):
        add_mecanico = ("UPDATE tbl_mecanicos SET rut = %s, nombres = %s, apellidos = %s, correo = %s, telefono = %s, "
                    " direccion = %s, comuna = %s"
                    " WHERE rut = %s")

        data_mecanico = (M.getRut(), M.getNombres(), M.getApellidos(), M.getCorreo(), M.getTelefono(), M.getDireccion(), M.getComuna(), Rut)

        cursor = self.cnx.cursor()
        cursor.execute(add_mecanico, data_mecanico)
        self.cnx.commit()

    def ListarClientes(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM tbl_clientes")
        lista = []
        for(rut, nombres, apellidos, correo, telefono, direccion, comuna) in cursor:
            C = Cliente(rut, nombres, apellidos, correo, telefono, direccion, comuna)
            lista.append(C)
        return lista

    def ListarMecanicos(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM tbl_mecanicos")
        lista = []
        for(rut, nombres, apellidos, correo, telefono, direccion, comuna) in cursor:
            M = Mecanico(rut, nombres, apellidos, correo, telefono, direccion, comuna)
            lista.append(M)
        return lista


    def InsertarVehiculo(self, V):
        add_vehiculo = ("insert into tbl_autos"
                        "(patente, marca, modelo, year, color, numero_chasis, rut_cliente)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_vehiculo = (V.getPatente(), V.getMarca(), V.getModelo(), V.getYear(), V.getColor(), V.getChasis(), V.getCliente())

        cursor = self.cnx.cursor()
        cursor.execute(add_vehiculo, data_vehiculo)
        self.cnx.commit()


    def ListarVehiculos(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM tbl_autos")
        lista = []
        for(patente, marca, modelo, year, color, numero_chasis, rut_cliente) in cursor:
            A = Auto(patente, numero_chasis,color, marca, year, modelo, rut_cliente)
            lista.append(A)
        return lista

    def UpdateCliente(self, C, rut):
        cursor = self.cnx.cursor()
        add_cliente = ("update tbl_clientes"
        " set rut = %s, nombres = %s, apellidos = %s, direccion = %s, correo = %s, telefono = %s, comuna = %s"
        f" where rut = {rut}")

        data_cliente = (C.getRut(), C.getNombres(), C.getApellidos(), C.getDireccion(), C.getCorreo(), C.getTelefono(), C.getComuna())

        cursor = self.cnx.cursor()
        cursor.execute(add_cliente, data_cliente)
        self.cnx.commit()
        


    

#CREATE
#RUD