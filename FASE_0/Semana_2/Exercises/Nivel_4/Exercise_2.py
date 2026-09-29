#Cambio de moneda: pide un monto en pesos y una tasa de cambio, y muestra cuántos dólares son, con 2 decimales.

dolar= 3.056,00

moneda_local = float(input("Ingrese el monto que desea cambiar a dolares: "))
transaccion = moneda_local // dolar

print(f"El cambio a dolares es de: {transaccion} dolares")

##OTRA FORMA DE HACERLO

pesos = float(input("Ingrese el monto en pesos: "))
tasa_dolar = float(input("Ingrese cuantos pesos vale 1 dolar: "))

dolares = pesos / tasa_dolar

print(f"{pesos:,.2f} pesos son {dolares:,.2f} dolares")