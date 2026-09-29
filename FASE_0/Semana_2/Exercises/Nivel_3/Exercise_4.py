#Pide un precio y muestra el precio con IVA (constante IVA = 0.19) con 2 decimales.

IVA = 0.19

producto = input("Ingrese el nombre del producto que va a llevar: ")
precio_producto = float(input("Ingrese el costo del producto: "))
incremento_IVA = precio_producto * IVA
precio_final = precio_producto + incremento_IVA
print(f"El precio final del producto con la suma del IVA es de: {precio_final:.2f}")