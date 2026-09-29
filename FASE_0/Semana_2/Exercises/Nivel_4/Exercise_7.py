#Área y perímetro: pide base y altura de un rectángulo y muestra área y perímetro. Luego haz lo mismo con un círculo a partir del radio (usa 3.14159).
import math
#
# #AREA Y PERIMETRO DEL RECTANGULO
##area = base*altura
#perimetro = 2(altura+base)

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area_rectangulo = base * altura 
perimetro_rectangulo = area_rectangulo * 2

print(f"El perimetro del rectangulo es: {perimetro_rectangulo} y el area del perimetro es: {area_rectangulo}")


##AREA Y PERIMETRO DEL CIRCULO
#perimetro = 2*pi*radio
#area = pi*radio²

radio = float(input("Ingrese el radio del circulo: "))

perimetro_circulo = 2*math.pi*radio
area_circulo = math.pi*radio**2

print(f"El perimetro del circulo es: {perimetro_circulo} y el area del circulo es: {area_circulo}")


##OTRA FORMA DE HACERLO

import math

# Rectángulo
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area_rectangulo = base * altura
perimetro_rectangulo = 2 * (base + altura)

print(f"Rectangulo -> area: {area_rectangulo:.2f}, perimetro: {perimetro_rectangulo:.2f}")

# Círculo
radio = float(input("Ingrese el radio del circulo: "))

area_circulo = math.pi * radio ** 2
perimetro_circulo = 2 * math.pi * radio

print(f"Circulo -> area: {area_circulo:.2f}, perimetro: {perimetro_circulo:.2f}")
