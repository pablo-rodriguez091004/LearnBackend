#Segundos a horas: pide un total de segundos y muestra cuántas horas, minutos y segundos son. Pista: usa // y %.

minuto = 60

#INGRESO DE DATOS
segundos = int(input("Ingrese los segundos deseados: "))

#PROCESO A REALIZAR

segundos_a_horas =  (segundos * 1) / 3600
segundos_a_minutos = (segundos * 1) / 60
segundos_a_segundos = (segundos * minuto) / minuto

#CODIGO DE SALIDA

print(f"Los {segundos} que ha ingresado se ven de la siguiente forma: {segundos} son: {segundos_a_horas} horas, {segundos} son {segundos_a_minutos} minutos y {segundos} son: {segundos_a_segundos} segundos")

print(segundos_a_horas)
print(segundos_a_minutos)
print(segundos_a_segundos)


##OTRA FORMA DE HACERLO 

SEGUNDOS_POR_HORA = 3600
SEGUNDOS_POR_MINUTO = 60

total_segundos = int(input("Ingrese los segundos: "))

horas = total_segundos // SEGUNDOS_POR_HORA
resto = total_segundos % SEGUNDOS_POR_HORA

minutos = resto // SEGUNDOS_POR_MINUTO
segundos = resto % SEGUNDOS_POR_MINUTO

print(f"{total_segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")