class Menu:
    def __init__(self, mensajeDeBienvenida):
        self.mensajeDeBienvenida = mensajeDeBienvenida

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("--- Menu del Banco ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Que numero de opcion quieres? ")
        return opcion

    def procesaOpcion(self, opcion, cuenta):
        if opcion == '1':
            print("Titular:", cuenta.titular)
            print("Saldo:", cuenta.cantidad)
        elif opcion == '2':
            monto = float(input("Cuanto vas a depositar? "))
            cuenta.depositar(monto)
        elif opcion == '3':
            monto = float(input("Cuanto vas a retirar? "))
            cuenta.retirar(monto)
        elif opcion == '4':
            print("Adios")
        else:
            print("Opcion incorrecta")