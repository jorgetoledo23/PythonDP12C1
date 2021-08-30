class Auto:
    # Atributos / Campos
    patente = None
    nChasis = None
    color = None
    marca = None
    year = None
    estadoMotor = False #False Off / True On

    def avanzar():
        pass

    def encenderMotor(self, tipo, nombre):
        self.estadoMotor = True

    def getEstado(yoMismo):
        if yoMismo.estadoMotor == False: return False
        else: return True






class Mecanico:
    pass

class Reparacion:
    pass


