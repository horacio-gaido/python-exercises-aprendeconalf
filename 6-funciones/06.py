"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
lista_1 = [1,2,3,4,5,6,7,8,9,10]

def avg (lista_1):
    suma = 0
    for i in lista_1:
        suma += i
    avg = suma / len(lista_1)
    return avg


print(avg (lista_1))


