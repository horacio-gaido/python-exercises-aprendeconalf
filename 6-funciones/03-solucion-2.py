"""Función que calcula el factorial de un número entero positivo.
Parámetros
n: Es un entero positivo.
Devuelve el factorial de n.

c *= a is equivalent to     c = c * a
tmp *= i+1  is equivalent to    tmp = tmp * (i + 1)


def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial(4))


"""
n = 4 
tmp = 1
for i in range(n):
    tmp *= i+1

print(tmp)