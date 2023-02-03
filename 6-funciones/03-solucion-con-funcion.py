"""
https://www.delftstack.com/es/howto/python/python-factorial/
Calcular el factorial de un número usando recursión en Python
La recursión no es más que llamar a la misma función una y otra vez. 
Usando la recursión, podemos escribir menos líneas de código, que serán mucho más legibles que el código que escribiremos usando el método iterativo.
Cada vez que llamamos a una función de recursión, se crea una pila de recursión en la memoria. 
Esta pila de recursividad tiene algo llamado contador de programa, que lleva la cuenta de la siguiente instrucción a ejecutar 
después de que la función de recursividad termine su ejecución.

"""

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

num = 5
print("Factorial of",num,"is", factorial(num))