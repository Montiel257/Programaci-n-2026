"""
Created on Marzo, 2026
@author: Montiel257
"""

class Menu:

    def __init__(self, mensaje):
        self.__mensaje = mensaje

    def bienvenida(self):
        print(self.__mensaje)

    def opciones(self):
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Mostrar cuenta")
        print("4. Salir")
        return input("Opcion: ")
