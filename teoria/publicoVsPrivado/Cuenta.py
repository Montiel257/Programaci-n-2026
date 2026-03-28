"""
Created on Marzo, 2026
@author: Montiel257
"""

class Cuenta:

    def __init__(self, saldo, tipo, fechaCreacion):
        self.__saldo = saldo
        self.__tipo = tipo
        self.__fechaCreacion = fechaCreacion

    def depositar(self, cantidad):
        if cantidad <= 0:
            return False
        self.__saldo += cantidad
        return True

    def retirar(self, cantidad):
        # MÉTODO PÚBLICO
        if cantidad > self.__saldo:
            return False
        self.__saldo -= cantidad
        return True

    def getSaldo(self):
        return self.__saldo

    def getTipo(self):
        return self.__tipo

    def __str__(self):
        return "Saldo: " + str(self.__saldo) + ", Tipo: " + self.__tipo
