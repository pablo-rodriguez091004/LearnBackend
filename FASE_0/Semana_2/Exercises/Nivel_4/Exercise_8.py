#Propina: pide el valor de una cuenta y un porcentaje de propina, y muestra la propina y el total

valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
#la propina sera del 40%
porcentaje_propina = (0.40 * 100)/valor_cuenta
cuenta_con_propina = valor_cuenta - porcentaje_propina
cuenta_final_propina = cuenta_con_propina

print(f"El valor de la cuenta sin propina es de: {valor_cuenta} y el valor de la cuenta con propina es de: {cuenta_final_propina}")


##OTRA FORMA DE HACERLO


valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

propina = valor_cuenta * porcentaje_propina / 100
total = valor_cuenta + propina

print(f"Propina: {propina:,.2f}")
print(f"Total a pagar: {total:,.2f}")