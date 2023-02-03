"""
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

word = str(input("Introduca una palabra para verificar el número de veces que contiene cada vocal: "))
counter_a = 0
counter_e = 0
counter_i = 0
counter_o = 0
counter_u = 0

for i in word:
    if i == "a":
        counter_a += 1
        print (f"La palabra {word} tiene {counter_a} vez / veces la letra a")
for i in word:
    if i == "e":
        counter_e += 1
        print (f"La palabra {word} tiene {counter_e} vez / veces la letra e")
for i in word:
    if i == "i":
        counter_i += 1
for i in word:
        print (f"La palabra {word} tiene {counter_i} vez / veces la letra i")
for i in word:
    if i == "o":
        counter_o += 1
        print (f"La palabra {word} tiene {counter_o} vez / veces la letra o")
for i in word:
    if i == "u":
        counter_u += 1
        print (f"La palabra {word} tiene {counter_u} vez / veces la letra u")