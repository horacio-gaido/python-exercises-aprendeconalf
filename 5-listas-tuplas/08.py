"""
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

def palindromo(word):
    word = word.replace(" ", "")
    word = word.lower()
    word_reversed = word[::-1]
    if word_reversed == word:
        return True
    else:
        return False

def run():
    word = str(input("Introduca una palabra para verificar si es un palíndromo: "))
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print ("Esta palabra ES un palindromo")
    else:
        print ("Esta palabra NO es un palindromo")

if __name__ == '__main__':
    run()
