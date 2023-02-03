"""
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

"""

frase = input("Introduzca una frase: ")
vocal1 = input("Introduzca una vocal: ")
vocal2 = vocal1.upper()
frase2 = frase.replace(vocal1, vocal2)
print(frase2)









