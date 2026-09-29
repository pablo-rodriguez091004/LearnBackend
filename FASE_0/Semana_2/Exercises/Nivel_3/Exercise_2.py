#Pide tu año de nacimiento y calcula tu edad aproximada (año actual menos año de nacimiento). Recuerda convertir con int().

AÑOACTUAL = 2026
fecha_nacimiento = int(input("Ingrese el año de su nacimiento: "))
edad_usuario = AÑOACTUAL -fecha_nacimiento  
print(f"Su edad actual es: {edad_usuario} años ")