class Auto:
    # Atributos / Campos

    #Metodo Constructor
    def __init__(self, pat, chas, col, mar, year, modelo):
        self.__patente = str(pat).upper()
        self.nChasis = chas
        self.__color = col
        self.marca = str(mar).upper()
        self.modelo = str(modelo).upper()
        self.year = year

    #Encapsular
    def getPatente(self):
        return self.__patente

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getInfo(self):
        return f"AUTO PATENTE {self.__patente},NCHASIS: {self.nChasis}, MARCA: {self.marca}, MODELO: {self.modelo}, COLOR: {self.getColor()}, AÑO: {self.year}"

class Mecanico:
    
    def __init__(self, rut,nom, ape, edad, direccion):
        self.rut = rut
        self.edad = edad
        self.nombres = str(nom).upper()
        self.apellidos = str(ape).upper()
        self.direccion = str(direccion).upper()

        if(edad >= 18):
            self.mayorEdad = True
        else:
            self.mayorEdad = False

    def getInfo(self):
        return f"RUT: {self.rut}, NOMBRES: {self.nombres}, APELLIDOS: {self.apellidos}"


class Reparacion:
    
    def __init__(self, auto, mecanico, valor):
        self.vehiculoReparacion = auto
        self.mecanicoReparacion = mecanico
        self.valor = valor


    def getInfo(self):
        return f"INFO REPARACION! AUTO: {self.auto.getInfo()}, MECANICO: {self.mecanico.getInfo()}"

