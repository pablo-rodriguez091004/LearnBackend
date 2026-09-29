#Pide dos números y muestra suma, resta, multiplicación, división, división entera, resto y potencia (primero ** segundo).
first_number = int(input("Ingrese el primer numero: "))
second_number = int(input("Ingrese el segundo numero: "))

suma = first_number + second_number
resta = first_number - second_number
multiplicacion = first_number * second_number
division = first_number / second_number
division_entera = first_number // second_number
resto = first_number % second_number
potencia = first_number ** second_number

print(f"Los resultados fueron los siguientes: suma: {suma}; resta: {resta}; multiplicacion: {multiplicacion}; division: {division}; division_enteda: {division_entera}; resto: {resto}; potencia: {potencia}")