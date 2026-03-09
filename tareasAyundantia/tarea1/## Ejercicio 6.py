## Ejercicio 6

print("Primero 100 numeros de la sucesión de Fibonacci")

n = 100

a = 1
b = 1

print(f"Los primeros {n} términos de la sucesión de Fibonacci son:")

for i in range(n):
    print(f"Término {i + 1}: {a}")
    
    a, b = b, a + b

print("¡Sucesión terminada!")