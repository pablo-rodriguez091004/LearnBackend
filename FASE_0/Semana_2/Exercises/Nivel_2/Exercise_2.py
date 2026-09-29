# Reescribe con nombres claros y una constante:
"""
   x = 100000
   y = 0.19
   z = x * y
   w = x + z
"""""

IVA = 0.19
precio_base = 100000
valor_iva = precio_base * IVA
precio_total = precio_base + valor_iva
print(f"Precio total: {precio_total}")