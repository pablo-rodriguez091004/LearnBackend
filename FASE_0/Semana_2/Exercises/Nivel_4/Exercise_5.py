#Descuento: pide un precio y un porcentaje de descuento, y muestra el ahorro y el precio final.

print("¡HOY TODO ARTICULO TIENE UN 30% DE DESCUENTO!")

precio = float(input("Ingrese el precio del producto a llevar: "))

descuento = 0.30

precio_descuento = precio * descuento

precio_final = precio - precio_descuento

ahorro = precio_descuento

print(f"El precio original del producto es de: {precio} mil pesos, pero con el descuento el producto quedara costando: {precio_final}, usted ha ahorrado {ahorro} pesos")


##OTRA FORMA DE HACERLO

precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

ahorro = precio * porcentaje_descuento / 100
precio_final = precio - ahorro

print(f"Precio original: {precio:,.2f} pesos")
print(f"Ahorro: {ahorro:,.2f} pesos")
print(f"Precio final: {precio_final:,.2f} pesos")