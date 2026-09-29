#Crea una variable llamada sum, úsala, y luego intenta sum([1, 2, 3]). Explica con tus palabras qué pasó y cómo se arregla.

# paso 1: sum es la función de Python y funciona
print(sum([1, 2, 3]))     # 6

# paso 2: creo mi variable con el mismo nombre
sum = 10
print(sum)                # 10

# paso 3: la variable tapó a la función (esto da error, ejecútalo y lee el mensaje)
# print(sum([1, 2, 3]))   # TypeError: 'int' object is not callable

# paso 4: arreglo 1: borro mi variable y la función vuelve
del sum
print(sum([1, 2, 3]))     # 6