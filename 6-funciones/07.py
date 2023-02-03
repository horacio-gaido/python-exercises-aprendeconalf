"""
Ejercicio 7
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

"""
lista = [1,2,3,4,5]
cuadrados = [i**2 for i in lista]
print(cuadrados)


sample = [1,2,3,4,5]
def square (sample):
    square_list = []
    for i in sample:
        sample.append(i ** 2)
    return square_list

print(square(sample))