from Cuenta import Cuenta
from Menu import Menu

class Main:
    pass

if __name__ == "__main__":
    mi_cuenta = Cuenta(3000, 5000)
    mi_menu = Menu()

    mi_menu.darBienvenida()
    
    opcion = ""
    while opcion != "4":
        opcion = mi_menu.despliegaMenu()
        if opcion != "4":
            mi_menu.procesaOpcion(opcion, mi_cuenta)
            
    print("Gracias por usar el sistema.")
