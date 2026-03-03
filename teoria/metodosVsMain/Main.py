from Cuenta import Cuenta
from Menu import Menu

class Main:
    pass

# Ejecución del algoritmo principal
if __name__ == "__main__":
    # 1. Creamos los objetos
    mi_cuenta = Cuenta(3000, 5000)
    mi_menu = Menu()

    # 2. Usamos los métodos
    mi_menu.darBienvenida()
    
    opcion = ""
    while opcion != "4":
        opcion = mi_menu.despliegaMenu()
        if opcion != "4":
            mi_menu.procesaOpcion(opcion, mi_cuenta)
            
    print("Gracias por usar el sistema.")
