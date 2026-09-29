#Intercambia los valores de x = 3 e y = 7 usando una variable auxiliar. Luego busca cómo hacerlo en una sola línea (x, y = y, x) y comprueba que da lo mismo.

x = 3
y = 7

changue_variable = 4

x = x + changue_variable
y = y - changue_variable

print(f"El valor de x es: {x} y el valor de y es: {y}")

x = 10
y = 2
# con tu método: x = 14, y = -2   -> mal

x = 3
y = 7

auxiliar = x     # guardo el valor de x antes de perderlo
x = y            # x toma el valor de y
y = auxiliar     # y toma el valor guardado de x

x, y = y, x

print(f"El valor de x es: {x} y el valor de y es: {y}")

# --- Método 1: variable auxiliar ---
x = 10
y = 2
print(f"Antes:   x = {x}, y = {y}")

auxiliar = x
x = y
y = auxiliar
print(f"Después: x = {x}, y = {y}")

# --- Método 2: asignación múltiple ---
x = 10
y = 2
print(f"Antes:   x = {x}, y = {y}")

x, y = y, x
print(f"Después: x = {x}, y = {y}")