## Ejercicio 4

import random

sucesion = []
suma_total = 0.0
limite = 1.50

print("Generando la sucesión...")

while True:
    nuevo_numero = random.uniform(0.01, 0.20)
    
    if suma_total + nuevo_numero < limite:
        sucesion.append(nuevo_numero)
        suma_total += nuevo_numero
    else:
    	break

print(f"Se generaron {len(sucesion)} números en total.")

print("Los números son:")
for i, num in enumerate(sucesion):
    print(f"Número {i+1}: {round(num, 4)}")

print(f"La suma total es: {round(suma_total, 4)}")