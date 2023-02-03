"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

"""

table = int(input("Ingrese el número correspondiente a la tabla de multiplicar que quiere ver del 1 al 10: "))
for i in range(11):
    print(f"{i} x {table} = {table * i}")