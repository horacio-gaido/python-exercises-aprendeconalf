word = str(input("Introduca una palabra para verificar si es un palíndromo: "))
word = word.replace(" ", "")
word = word.lower()
word = word.strip()
word_reversed = word[::-1]
if word_reversed == word:
    print ("Esta palabra ES un palindromo")
else:
    print ("Esta palabra NO es un palindromo")


