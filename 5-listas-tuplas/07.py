"""
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

"""

alphabet = []
while True:
    letters = str(input("Ingrese las letras del abcedario, cuando termine escriba el nombre 'salir' para terminar:  "))
    alphabet.append(letters)
    if letters == "salir":
        print()
        alphabet.remove("salir")
        break
new_alphabet = alphabet[2::3]
alphabet_3 = alphabet.remove(new_alphabet)





