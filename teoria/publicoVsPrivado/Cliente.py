"""
Created on Marzo, 2026
@author: Montiel257
"""

class Cliente:

    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def __str__(self):
        return "Cliente: " + self.nombre + " | " + self.cuenta.getTipo() + " | Saldo: " + str(self.cuenta.getSaldo())
