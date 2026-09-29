#Conversor de temperatura: pide grados Celsius y muestra Fahrenheit (F = C * 9/5 + 32) y Kelvin (K = C + 273.15).

CELSISUS = float(input("Ingrese la temperatura en la que se encuentra ahora: "))

FAHRENHEIR = (CELSISUS * 9/5) + 32 
KELVIN = CELSISUS + 273.15

print (f"La temperatura en grados Fahrenheit es de: {FAHRENHEIR} y en grados Kelvin es de: {KELVIN}")

##OTRA FORMA DE HACERLO

celsius = float(input("Ingrese los grados Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Kelvin: {kelvin:.2f}")