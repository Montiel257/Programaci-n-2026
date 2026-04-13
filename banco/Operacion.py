
class Inversion:

  def __init__(self, valor1, valor2, valor3, valor4):
    self.saldo = valor1
    self.rendimiento = valor2
    self.tiempo = valor3
    self.empresa = valor4
  
  def depositar(self, cantidad):
    self.saldo=self.saldo + cantidad

  def retirar(self, cantidad):
    self.saldo=self.saldo - cantidad
 
  
  def calcular(self):
    monto = self.capital * (1 + self.rendimiento * self.tiempo)

  def mostrar(self):
        print("Nombre de la empresa:", self.empresa)
        print("Saldo actual:", self.saldo)
        print("Rendimiento:", self.rendimiento)
        print("Tiempo:", self.tiempo, "meses")
