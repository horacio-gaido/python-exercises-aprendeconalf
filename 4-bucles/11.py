"""
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

"""

word = str(input("Ingrese una palabra: "))
word_2 = word[::-1]

for i in word_2:
    print(i)
