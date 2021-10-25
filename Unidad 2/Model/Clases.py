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
