# Autor: Samuel Emiliano Perez Montiel
# Descripción: Archivo principal que coordina la ejecución de las clases.

from Cuenta import Cuenta
from Menu import Menu

class Main:
    """Clase principal vacía según requerimiento"""
    pass

if __name__ == "__main__":
    # 1. Crear el objeto Cuenta (los datos de la cuenta)
    mi_cuenta = Cuenta(3000, "Ahorro", "01/01/2023")
    
    # 2. Crear el objeto Menu
    mi_menu = Menu("BIENVENIDO A BANCOS MONTILIANOS")
    
    # 3. Ejecutar flujo
    mi_menu.dar_bienvenida()
    
    # El ciclo permite que el usuario haga varias cosas sin que el programa se cierre
    opcion_elegida = ""
    while opcion_elegida != "4":
        opcion_elegida = mi_menu.despliegaMenu()
        mi_menu.procesaOpcion(opcion_elegida, mi_cuenta)
