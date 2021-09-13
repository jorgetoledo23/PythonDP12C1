import os
class MenuPrincipal:

    def MostrarMenu(self):
        #self.LimpiarConsola()
        print("----------------------------------------")
        print("Seleccione una Opcion: ")

        print("Presione 1 para agregar Autos")
        print("Presione 2 para agregar Mecanicos")
        print("Presione 3 para agregar Reparacion")

        print("Presione 4 para ver los Autos")
        print("Presione 5 para ver los Mecanicos")
        print("Presione 6 para ver las Reparaciones")

        print("Presione 0 para Salir")

    def LimpiarConsola(self):
        os.system('cls' if os.name=='nt' else 'clear')