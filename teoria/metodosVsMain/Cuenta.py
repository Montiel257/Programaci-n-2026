# Autor: Samuel Emiliano Perez Montiel
# Fecha: 03 de febrero de 2026
# Descripción: Clase que gestiona el saldo y operaciones de una cuenta bancaria.

class Cuenta:
    def __init__(self, saldo, tipo, fecha_creacion):
        """Constructor que inicializa los atributos de la cuenta"""
        self.saldo = saldo
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion

    def informacion(self):
        """Muestra los detalles actuales de la cuenta"""
        print(f"Saldo actual: {self.saldo}")
        print(f"Tipo de cuenta: {self.tipo}")
        print(f"Fecha de creación: {self.fecha_creacion}")

    def retirar(self, cantidad):
        """Resta una cantidad al saldo actual"""
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Error: Fondos insuficientes.")

    def depositar(self, cantidad):
        """Suma una cantidad al saldo actual"""
        self.saldo += cantidad
