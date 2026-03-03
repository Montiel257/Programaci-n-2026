class Menu:
    def __init__(self):
        self.mensajeDeBienvenida = "¡Bienvenido a Bancos Montilianos!"

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar Saldo")
        print("4. Salir")
        return input("Elige una opción: ")

    def procesaOpcion(self, opcion, cuenta):
        if opcion == "1":
            monto = float(input("Cantidad a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "2":
            monto = float(input("Cantidad a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":
            print(f"Tu saldo actual es: {cuenta.saldo}")
        else:
            print("Opción no válida o saliendo...")
