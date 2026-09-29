"""
BUENAS PRACTICAS EN PYTHON - guia de consulta rapida
Semana 2 - Fase 0
"""

# =========================================================
# 1. PEDIR DATOS
# =========================================================
# - el mensaje va dentro de input(): una sola instruccion, misma linea.
# - deja un espacio al final del mensaje para que la respuesta no quede pegada.
# - input() SIEMPRE devuelve texto: no uses str(input()), sobra.
# - para numeros, convierte en la misma linea: int() o float().
# - int("abc") da ValueError (mas adelante se controla con try/except).

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
precio = float(input("Ingrese el precio: "))

# MAL:  print("Ingrese su nombre: ")
#       nombre = input ()

# =========================================================
# 2. MOSTRAR DATOS
# =========================================================
# - usa f-strings: f"...{variable}..."
# - se leen como la frase final, no necesitan str() y no hay que
#   acordarse de los espacios (con "+" los pones tu, con comas Python
#   los pone solo).
# - dentro de las llaves puedes operar y dar formato.

print(f"Hola, {nombre}. Tienes {edad} anos.")
print(f"Dentro de 10 anos tendras {edad + 10}.")
print(f"Precio: {precio:.2f}")        # 2 decimales
print(f"Precio: {precio:,.2f}")       # 2 decimales y separador de miles

# MAL:  print("Hola " + nombre + " tienes " + edad)   # TypeError
# OK:   print("Hola", nombre, "tienes", edad)         # funciona, pero menos claro

# =========================================================
# 3. NOMBRES
# =========================================================
# - variables y funciones: snake_case -> primer_nombre, precio_total
# - clases: PascalCase -> FirstName (se ve en la semana de POO)
# - constantes: MAYUSCULAS -> IVA = 0.19
# - el nombre debe decir que guarda: edad_usuario, no x ni dato1.
# - elige un idioma (espanol o ingles) y no lo mezcles en el proyecto.
# - no empieza con numero, sin espacios ni simbolos, ni palabras
#   reservadas (if, for, class, True, None...).
# - Python distingue mayusculas: edad y Edad son variables distintas.

IVA = 0.19

# =========================================================
# 4. FORMATO (PEP 8)
# =========================================================
# - sin espacio entre funcion y parentesis: print(x), input()
# - espacios alrededor de = y operadores: a = b + c
# - una instruccion por linea.
# - lineas de maximo ~79-88 caracteres.
# - 4 espacios de indentacion, nunca mezclar con tabs.
# - dos lineas en blanco entre funciones.
# - que lo formatee una herramienta: pip install ruff
#   luego: ruff format archivo.py

# MAL:  x=a+b ;print (x)
# OK:   suma = a + b
#       print(suma)

# =========================================================
# 5. COMENTARIOS
# =========================================================
# - explica el POR QUE, no el QUE (el codigo ya dice lo que hace).
# - cortos y en minuscula normal, no en mayusculas.
# - si un comentario hace falta para entender que hace una linea,
#   mejor renombra la variable o la funcion.

# MAL:  intentos += 1   # suma 1 a intentos
# OK:   intentos += 1   # cuenta el intento fallido

# =========================================================
# 6. CODIGO LIMPIO: REGLAS GENERALES
# =========================================================
# 1. nombres que dicen que guardan.
# 2. formato estandar (PEP 8) con ruff.
# 3. una instruccion por linea.
# 4. sin codigo repetido: si copias y pegas 3 veces, va en una funcion.
# 5. constantes al inicio del archivo, en mayusculas.
# 6. funciones cortas que hacen UNA sola cosa.
# 7. cada archivo con un solo proposito.
# 8. probar el codigo (pytest) antes de subirlo a git.

# =========================================================
# 7. ERRORES COMUNES
# =========================================================
# NameError   -> variable que no existe o mal escrita (Edad vs edad)
# TypeError   -> mezclar tipos incompatibles ("5" + 3)
# ValueError  -> valor no convertible (int("abc"))
# SyntaxError -> falta una comilla, parentesis o dos puntos
# - lee siempre el mensaje completo: dice el tipo de error y la linea.

# =========================================================
# 8. ORDEN RECOMENDADO DE UN ARCHIVO
# =========================================================
# 1. docstring del archivo (que hace)
# 2. imports
# 3. constantes
# 4. funciones
# 5. codigo principal