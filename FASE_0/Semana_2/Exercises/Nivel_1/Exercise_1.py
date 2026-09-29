#Crea variables con tu nombre, edad, ciudad y altura en metros, y muéstralas en una sola frase con f-string.

first_name = input("Ingrese su primer nombre: ") ## CUADNO USAMOS EL INPUT AUTOMATICAMENTE SE CONVIERTE EN STRING, NO HACE FALTA PONER STR()
second_name = input("Ingrese su segundo nombre: ")
first_last_name = input("Ingrese su primer apellido: ")
second_last_name = input("Ingrese su segundo apellido: ") 
height = float(input("Ingrese su altura en metros: ")) ## - para numeros, convierte en la misma linea: int() o float(). 
age = int(input("Ingrese su edad: ")) ## CUANDO USAMOS EL INPUT AUTOMATICAMENTE SE CONVIERTE EN STRING, POR ESO HAY QUE CONVERTIRLO A INT() PARA PODER OPERAR CON EL
location = input("Ingrese su lugar de residencia: ")
phone_number = input("Ingrese su número de teléfono: ")


print(f"Hola, {first_name} {second_name} {first_last_name} {second_last_name}")
print(f"Tienes {age} años y vives en {location}. Tu número de teléfono es: {phone_number}")
print(f"Tu altura es: {height} metros")