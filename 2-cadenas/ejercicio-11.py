"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""


producto = str(input("Ingrese el nombre del producto: "))
precio = round((float(input("Ingrese el precio del producto: "))),2)
cantidad = int(input("Ingrese el la cantidad del producto: "))
costo_total = round((precio * cantidad),2)

print(f"El nombre del producto es {producto}, su precio unitario es {precio}, la cantidad de unidades es {cantidad} y el coste total es {costo_total}")