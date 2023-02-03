"""
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
"""

a = 28
lista = []
lista_2 = []
contador = a

while contador > 0:
    if a % 2 == 0:
        lista.append (0)
        contador /= 2

    else:
        lista.append (1)
        contador /= 2

print(lista)
print(lista_2)