''' 
Created on Febrero,2026 
@author: Montiel257

'''
from Cuenta import *

class Pruebas:
	pass

print ("Desde las pruebas")

cuenta1 = Cuenta( 300, 'C', "Samuel Perez" )
cuenta2 = Cuenta(6222, 'D', "Yaret Vargas")

print ("DATOS DE LA CUENTA 1")
print (cuenta1.cantidad)
print (cuenta1.tipo)
print (cuenta1.titular)

print ("DATOS DE LA CUENTA 2")
print (cuenta2.cantidad)
print (cuenta2.tipo)
print (cuenta2.titular)