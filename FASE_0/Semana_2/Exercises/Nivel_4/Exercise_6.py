#Dígitos: pide un número de 3 cifras y muestra cada dígito por separado. Pista: % y // con 10 y 100. Ejemplo: 472 da 4, 7, 2.

numero = int(input("Ingrese un numero de 3 cifras: "))

centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10

print(f"Centenas: {centenas}")
print(f"Decenas: {decenas}")
print(f"Unidades: {unidades}")