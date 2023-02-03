"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
N= 5
!N = 5x4x3x2x1
"""

import functools
number = int(input("Ingrese un número entero positivo:"))

print(functools.reduce((lambda x , y : x * y ) , range(1 , number+1)))

