from Cuenta import *
from Menu import *
from Cliente import *

class Main:
    pass

print("--- PROBANDO EL BANCO ---")

cuenta1 = Cuenta(300, 'C', "Samuel Perez")

mi_menu = Menu("Bienvenido al cajero automatico")
mi_menu.darBienvenida()

opcion_elegida = mi_menu.despliegaMenu()

mi_menu.procesaOpcion(opcion_elegida, cuenta1)

print("\n--- PROBANDO EL CLIENTE ---")
cliente1 = Cliente("Samuel", "Mi casa", 21)
cliente1.imprimirDetalles()