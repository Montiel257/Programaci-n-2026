class Cuenta:
    def __init__(self, valor, tipo, titular):
        self.cantidad = valor
        self.tipo = tipo
        self.titular = titular

    def depositar(self, monto):
        self.cantidad = self.cantidad + monto
        print("Depositaste:", monto)
        print("Tu nuevo saldo es:", self.cantidad)

    def retirar(self, monto):
        self.cantidad = self.cantidad - monto
        print("Retiraste:", monto)
        print("Tu nuevo saldo es:", self.cantidad)