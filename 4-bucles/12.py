"""
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

"""

phrase = str(input("Ingrese una frase: "))
letter = str(input("Ingrese una letra: "))

counter = 0
for i in phrase:
    if letter == i:
        counter += 1
print (f"La frase {phrase} contiene {counter} veces la letra {letter}")
