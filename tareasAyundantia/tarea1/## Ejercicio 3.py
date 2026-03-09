## Ejercicio 3

print("Detector de palindromos")

palabra = (input("Cual es tu palabra a evaluar?: "))
palabraLimpia = palabra.lower().replace(" ", "")
if palabraLimpia == palabraLimpia [::-1]:
	print("Si,",palabra, "es un palindromo")

else:
	print("No,", palabra, "no es un palindromo")