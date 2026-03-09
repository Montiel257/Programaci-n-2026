## Ejercicio 2

numero = input("Introduce un número entero positivo: ")
suma = 0

# .isdigit() asegura que solo sean enteros y el otro que sean positivos
if numero.isdigit() and int(numero) > 0:
    for digito in numero_str:
        suma += int(digito)  # Convierte cada letra/dígito a número y lo suma
        
    print(f"La suma de los dígitos de {numero} es: {suma}")
else:
    print("El número debe ser un entero positivo.")