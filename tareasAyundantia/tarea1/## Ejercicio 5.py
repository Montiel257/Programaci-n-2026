## Ejercicio 5

i)

numero = int(input("Introduce un número entero: "))

es_primo = True

if numero <= 1:
    es_primo = False 
else:
    limite = int(numero ** 0.5)
    for i in range(2, limite + 1):
        if numero % i == 0:
            es_primo = False 
            break 

if es_primo:
    print(f"El número {numero} SÍ es primo.")
else:
    print(f"El número {numero} NO es primo.")


ii)
n = int(input("Ingresa el número límite (N): "))

print(f"Los números primos hasta el {n} son:")

for numero_actual in range(2, n + 1):
    
    es_primo = True
    limite = int(numero_actual ** 0.5)
    
    for i in range(2, limite + 1):
        if numero_actual % i == 0:
            es_primo = False
            break
            
    if es_primo:
        print(numero_actual, end=" - ")

print("¡Búsqueda terminada!")