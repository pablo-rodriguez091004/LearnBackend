## EN PYTHON NO ES NECESARIO DECLARAR QUE TIPO DE DATO VA A SER UNA VARIABLE, YA QUE ESTO SE DETERMINA AUTOMATICAMENTE SEGUN EL VALOR QUE SE LE ASIGNE A LA MISMA

## AL MOMENTO DE ASIGNAR O CREAR VARIABLES LO QUE MEJOR SE DEBE HACER ES PONER NOMBRES BIEN DEFINIDOS, YA QUE ASI SABREMOS EN UN FUTURO QUE TIPO DE DATO ES LA VARIABLE Y PARA QUE SIRVE, ESTO AYUDA A QUE EL CODIGO SEA MAS FACIL DE LEER Y ENTENDER 

## PYTHON ES CASE SENTIVE, ESTO SIGNIFICA QUE SI DECLARAMOS UNA VARIABLE CON UN NOMBRE EN MINUSCULAS Y LUEGO CREAMOS O ASIGNAMOS UNA VARIABLE CON EL MISMO NOMBRE PERO EN MAYUSCULAS, ESTAS SERAN VARIABLES DISTINTAS

## UNA BUENA PRACTICA ES MANEJAR CAMELLCASE O SNAKECASE PARA LOS NOMBRES DE LAS VARIABLES, ESTO AYUDA A QUE EL CODIGO SEA MAS FACIL DE LEER Y ENTENDER

## PODEMOS USAR COMILLAS DOBLES O COMILLAS SIMPLES PARA ASIGNAR VALORES DE TIPO STRING A LAS VARIABLES, ESTO NO AFECTA EL FUNCIONAMIENTO DEL CODIGO

print("Tipos de variables y sus valores")

### VARIABLES DE TIPO STRING

print ("Variables de tipo string")

NOMBRE = "Alejandro"
NOMBRe = "Pablo"
Apellido = "Suarez"
Vocal = "a"


print("El nombre es: ", NOMBRE)
print("El nombre es: ", NOMBRe)     
print("El apellido es: ", Apellido)
print("La vocal es: ", Vocal)



## LAS DOS VARAIBLES SON DISTINTAS YA QUE PYTHON ES CASE SENTIVE, ESTO SIGNIFICA QUE SI DECLARAMOS UNA VARIABLE CON UN NOMBRE EN MINUSCULAS Y LUEGO CREAMOS O ASIGNAMOS UNA VARIABLE CON EL MISMO NOMBRE PERO EN MAYUSCULAS, ESTAS SERAN VARIABLES DISTINTAS

print("Variables tipos numericos")

NUMERO1 = 5 # TIPO INT
NUMERO2 = 10 # TIPO INT
NUMERO3 = 12.4 # TIPO FLOAT
NUMERO4 = 3508715234 # TIPO INT
print("El primer numero es: ", NUMERO1)
print("El segundo numero es: ", NUMERO2)
print("El tercer numero es: ", NUMERO3)
print("El cuarto numero es: ", NUMERO4)
print("Variables tipo booleano")


print("Variables tipo booleano")

verdadero = True
falso = False

print("El valor de la variable verdadero es: ", verdadero)
print("El valor de la variable falso es: ", falso)


## SI DESEA ESPECIFICAR EL TIPO DE DATO DE UNA VARIABLE AL MOMENTO DE ASIGNARLA LO PUEDE HACER MEDIANTE EL CASTEO 

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

print("El valor de la variable x es: ", x, " y podemos confirmar que es un tipo de variable ", type(x))
print("El valor de la variable y es: ", y, " y podemos confirmar que es un tipo de variable ", type(y))
print("El valor de la variable z es: ", z, " y podemos confirmar que es un tipo de variable ", type(z))

## SI DESEA HACER UNA ASIGNACION MULTIPLE DE VARIABLES EN UNA SOLA LINEA PUEDE HACERLO DE LA SIGUIENTE MANERA, LA UNICA CONDICIOPN ES QUE EL NUMERO DE VARIABLES Y EL NUMERO DE VALORES ASIGNADOS DEBE SER EL MISMO, SI NO SE CUMPLE ESTA CONDICION SE GENERARA UN ERROR Y PUEDEN SER DE TIPO STRING, NUMERICO O BOOLEANO

a, b, c = 5, 10, 15
print("El valor de la variable a es: ", a, " y podemos confirmar que es un tipo de variable ", type(a))
print("El valor de la variable b es: ", b, " y podemos confirmar que es un tipo de variable ", type(b))
print("El valor de la variable c es: ", c, " y podemos confirmar que es un tipo de variable ", type(c))

D,E,F = "HOLA", 102.46, False
print("El valor de la variable D es: ", D, " y podemos confirmar que es un tipo de variable ", type(D))
print("El valor de la variable E es: ", E, " y podemos confirmar que es un tipo de variable ", type(E))
print("El valor de la variable F es: ", F, " y podemos confirmar que es un tipo de variable ", type(F))

## PARA OBTENER INFORMACION ACERCA DE UNA VARIABLE Y SABER QUE TIPO DE VARIABLE ES LO HACEMOS DE LA SIGUIENTE MANERA, ESTO NOS DEVOLVERA EL TIPO DE DATO DE LA VARIABLE
print("El tipo de dato de la variable x es: ", type(x))
print("El tipo de dato de la variable y es: ", type(y))
print("El tipo de dato de la variable z es: ", type(z))
print("El tipo de dato de la variable D es: ", type(D))     