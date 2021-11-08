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

    def InsertarMecanico(self, M):
        add_mecanico = ("insert into tbl_mecanicos"
                        "(rut, nombres, apellidos, direccion, correo, telefono, comuna)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_mecanico = (M.getRut(), M.getNombres(), M.getApellidos(), M.getDireccion(), M.getCorreo(), M.getTelefono(), M.getComuna())

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
        


    

#CREATE
#RUD