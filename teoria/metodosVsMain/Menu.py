# Autor: Samuel Emiliano Perez Montiel
# Descripción: Clase encargada de la interacción y despliegue de opciones.

from Cuenta import Cuenta

class Menu:
    def __init__(self, mensaje):
        """Inicializa el mensaje de bienvenida"""
        self.mensaje = mensaje

    def dar_bienvenida(self):
        """Imprime el saludo inicial"""
        print(f"\n*** {self.mensaje} ***")

    def despliegaMenu(self):
        """Muestra las opciones y retorna la elección del usuario"""
        print("\n1. Retirar")
        print("2. Depositar")
        print("3. Información")
        print("4. Salir")
        return input("¿Qué desea hacer?: ")

    def procesaOpcion(self, opcion, cuenta):
        """Ejecuta la acción correspondiente según la opción elegida"""
        if opcion == "1":
            c = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(c)
            print(f"Nuevo saldo: {cuenta.saldo}")
            
        elif opcion == "2":
            c = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(c)
            print(f"Nuevo saldo: {cuenta.saldo}")
            
        elif opcion == "3":
            cuenta.informacion()
            
        elif opcion == "4":
            print("Saliendo del sistema...")
        else:
            print("Opción no válida.")
