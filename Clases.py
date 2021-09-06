class Auto:
    # Atributos / Campos

    #Metodo Constructor
    def __init__(self, pat, chas, col, mar, year):
        self.__patente = str(pat).upper()
        self.nChasis = chas
        self.__color = col
        self.marca = str(mar).upper()
        self.year = year
        self.estadoMotor = False

    def avanzar():
        pass

    def encenderMotor(self):
        self.estadoMotor = True

    def getEstado(yoMismo):
        if yoMismo.estadoMotor == False: return False
        else: return True

    #Encapsular
    def getPatente(self):
        return self.__patente

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

class Mecanico:
    
    def __init__(self, nom, ape, edad, direccion):
        self.edad = edad
        self.nombres = str(nom).upper()
        self.apellidos = str(ape).upper()
        self.direccion = str(direccion).upper()

        if(edad >= 18):
            self.mayorEdad = True
        else:
            self.mayorEdad = False


class Reparacion:
    
    def __init__(self, auto, mecanico):
        self.vehiculoReparacion = auto
        self.mecanicoReparacion = mecanico


    def getInfoReparacion(self):
        return "INFO REPARACION. Patente: " + self.vehiculoReparacion.getPatente() + " Marca: " + self.vehiculoReparacion.marca + ". MECANICO ASIGNADO: " + self.mecanicoReparacion.nombres

