#Pide un número y muestra su cuadrado, su cubo y su mitad. Intenta que cada valor aparezca en su propia línea.

numero_ejercicio = float(input("Ingrese un numero al azar: "))

cuadrado = numero_ejercicio ** 2
cubo = numero_ejercicio ** 3
mitad = numero_ejercicio / 2
mitad_exacta = numero_ejercicio // 2

print(f"El cuadrado del numero es: {cuadrado}; el dubo del numero es: {cubo}; la mitad del numero es: {mitad}; el modulo de la division del numero es: {mitad_exacta}")

print(f"Cuadrado: {cuadrado}")
print(f"Cubo: {cubo}")
print(f"Mitad: {mitad}")
print(f"Mitad entera: {mitad_exacta}")