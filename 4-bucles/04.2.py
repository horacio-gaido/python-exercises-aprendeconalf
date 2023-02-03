"""
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

"""

n = int(input("Introduce un número entero positivo: "))
print(type(n))

if n >= 0:
    for i in range(1, n+2):
        if i != n:
            print(n + 1 - i, end=", ")
        else: print(i - n - i + 1, end="")
else:
    print("Ha ingresado un valor incorrecto")