from Clases import Auto, Mecanico, Reparacion
import Menu

mecanicoJuan = Mecanico(nom="Juan Ignacio", ape="Toledo Valdes", edad=25, direccion="Merced 513, Curico")
M = Mecanico(nom="Daniel", ape="Fernandez Romero", edad=40, direccion="Yungai 1203, Curico")

A = Auto("jhhs34", "AJHSDHJAJSHD34231", "Azul", "kIa", "2013")
autoNissan = Auto("FGJK16", "YHGYHGGDFDGGSGFS34", "Rojo", "nIssAn", "2018")

reparacionKia = Reparacion(auto=A, mecanico=M)
print(reparacionKia.vehiculoReparacion.getColor())
reparacionKia.vehiculoReparacion.setColor("Blanco")
print(reparacionKia.vehiculoReparacion.getColor())


print(reparacionKia.getInfoReparacion())
# INFO REPARACION. Patente: JHHS34 Marca: KIA. MECANICO ASIGNADO: DANIEL
# INFO REPARACION. Patente: JHHS34 Marca: KIA. MECANICO ASIGNADO: DANIEL






