"""
Integrantes del equipo:

Samuel Emiliano Pérez Montiel
"""

'''
Created on May, 2026
@author: Montiel257
'''
"""
Manejo de errores
Conversión de calificaciones
"""

valor = input("Ingresa una calificación: ")

while valor != "":
    try:
        valor = int(valor)
        if valor == 10:
            print("La calificación en letra es: A+")
        elif valor == 9:
            print("La calificación en letra es: A")
        elif valor == 8:
            print("La calificación en letra es: B+")
        elif valor == 7:
            print("La calificación en letra es: B")
        elif valor == 6:
            print("La calificación en letra es: C")
        elif valor >= 0 and valor <= 5:
            print("La calificación en letra es: F")
        else:
            print("La entrada que ingresaste no es válida")

    except:
        try:
            valor = valor.upper()
            if valor == "A+":
                print("La calificación numérica es: 10")
            elif valor == "A":
                print("La calificación numérica es: 9")
            elif valor == "B+":
                print("La calificación numérica es: 8")
            elif valor == "B":
                print("La calificación numérica es: 7")
            elif valor == "C":
                print("La calificación numérica es: 6")
            elif valor == "F":
                print("La calificación numérica es: 5")
            else:
                raise ValueError

        except:
            print("La entrada proporcionada no es válida")
    valor = input("Ingresa una calificación: ")
print("El programa ha terminado")
