"""
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

number = int(input("Escriba un número entero positivo: "))
for i in range(1,number):
    if i % 2 != 0:
        print(i, end=", ")

