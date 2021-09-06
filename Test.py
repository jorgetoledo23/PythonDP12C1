#Test Script
from Clases import Auto

miAuto = Auto()



print("El estado del motor es: ", miAuto.getEstado())
miAuto.encenderMotor("Diesel", "V12")
print("El estado del motor es: ", miAuto.getEstado())

