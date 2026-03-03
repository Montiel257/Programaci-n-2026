class Cuenta:
    def __init__(self, valor, deuda):
        self.saldo = valor
        self.credito = deuda

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad_n):
        if cantidad_n <= self.saldo:
            self.saldo -= cantidad_n
            print("Retiro exitoso")
        else:
            print("Saldo insuficiente")
