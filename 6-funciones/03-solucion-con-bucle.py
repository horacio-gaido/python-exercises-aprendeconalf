"""
https://www.delftstack.com/es/howto/python/python-factorial/
Un factorial de un número es el producto de todos los enteros positivos menores o iguales a ese número. Por ejemplo, el factorial de 5 es el producto de todos los números que son menores e iguales a 5, es decir 5 * 4 * 3 * 2 * 1, que es igual a 120. Por lo tanto, el factorial del número 5 es 120.
Ahora vamos a escribir una función en Python para calcular el factorial de un número. 

Hay dos formas en las que podemos escribir un programa de factorial en Python, una utilizando el método de iteración y otra utilizando el método recursivo.

Calcular el factorial de un número usando la iteración en Python
El programa factorial usando el método de iteración no es más que usar bucles en nuestro programa como el bucle for o el bucle while. Al escribir un programa iterativo para el factorial en Python tenemos que comprobar tres condiciones.

El número dado es negativo: Si el número es negativo, entonces simplemente diremos que no podemos encontrar el factorial porque el factorial de un número negativo no existe.
El número dado es cero: Si el número es cero, entonces simplemente imprimiremos 1 porque el factorial de un número cero es 1.
Un número dado es positivo: Si el número es positivo, entonces sólo encontraremos su factorial.
"""

def factorial(num):
    if num < 0:
        print("Factorial of negative num does not exist")

    elif num == 0:
        return 1

    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

num = 5

print("Factorial of",num,"is", factorial(num))