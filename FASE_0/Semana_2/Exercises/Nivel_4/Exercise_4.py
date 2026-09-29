#Promedio: pide tres notas y muestra el promedio con 1 decimal.

nota1 = float(input("Ingrese las calificaciones del estudiante: "))
nota2 = float(input("Ingrese las calificaciones del estudiante: "))
nota3 = float(input("Ingrese las calificaciones del estudiante: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio fue: {promedio}")


##OTRA FORMA DE HACERLO

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio es: {promedio:.1f}")