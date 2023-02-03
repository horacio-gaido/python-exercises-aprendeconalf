"""
Ejercicio 10
Escribir un progracma que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

"""

precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()
print(precios)
mayor = precios[0]
menor = precios[len(precios)-1]
print(f"El mayor de los precios es {mayor}")
print(f"El menor de los precios es {menor}")