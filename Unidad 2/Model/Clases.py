class Auto:
    # Atributos / Campos

    #Metodo Constructor
    def __init__(self, pat, chas, col, mar, year, modelo):
        self.__patente = str(pat).upper()
        self.__nChasis = chas
        self.__color = col
        self.__marca = str(mar).upper()
        self.__modelo = str(modelo).upper()
        self.__year = year

    #Encapsular
    def getPatente(self):
        return self.__patente

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getInfo(self):
        return f"AUTO PATENTE {self.__patente},NCHASIS: {self.nChasis}, MARCA: {self.marca}, MODELO: {self.modelo}, COLOR: {self.getColor()}, AÑO: {self.year}"


class Persona:
    def __init__(self, rut, nombres, apellidos, correo, telefono, direccion, comuna):
        self.__rut = rut
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__correo = correo
        self.__telefono = telefono
        self.__direccion = direccion
        self.__comuna = comuna

    def getInfo(self):
        return f"Rut: {self.__rut} Nombres: {self.__nombres} Apellidos: {self.__apellidos}"

    def getInfoDetallada(self):
        return (f"Rut: {self.__rut} Nombres: {self.__nombres} Apellidos: {self.__apellidos}"
               f"Correo: {self.__correo} Telefono: {self.__telefono} Direccion: {self.__direccion}"
               f"Comuna: {self.__comuna}")
    def getRut(self):
        return self.__rut  
    def getNombres(self):
        return self.__nombres
    def getApellidos(self):
        return self.__apellidos  
    def getCorreo(self):
        return self.__correo  
    def getTelefono(self):
        return self.__telefono  
    def getDireccion(self):
        return self.__direccion  
    def getComuna(self):
        return self.__comuna

class Cliente(Persona):
    pass

class Mecanico(Persona):
    pass


import os
class MenuPrincipal:

    def MostrarMenu(self):
        print("=============== SISTEMA DE TALLER MECANICO ===============")
        print("===============   Seleccione una Opcion    ===============")
        print("")

        print("Presione 1 para gestionar Clientes")
        print("Presione 2 para gestionar Mecanicos")
        

        print("Presione 0 para Salir")

    def MenuSecundario(self, texto):
        print(f"===============      GESTION {texto}      ===============")
        print("===============   Seleccione una Opcion    ===============")
        print("")

        print(f"Presione 1 para Agregar {texto}")
        print(f"Presione 2 para Listar {texto}")
        print(f"Presione 3 para Editar {texto}")
        print(f"Presione 4 para Archivar {texto}")
        print(f"Presione 0 para Volver al Menu Principal")


    def LimpiarConsola(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def ConfirmacionIngreso(self, Objeto):
        input(f"{Objeto} Ingresado Exitosamente. Presione Enter para Continuar..." )

    def ConfirmacionEdit(self, Objeto):
        input(f"{Objeto} Editado Exitosamente. Presione Enter para Continuar..." )

    def ConfirmacionDelete(self, Objeto):
        input(f"{Objeto} Eliminado Exitosamente. Presione Enter para Continuar..." )