"""
Función recursiva que calcula el factorial
Tiene que recibir:
x=>El ultimo valor calculado
"""


def factorial(x,n):
	if (n > 0 ):
		# Se va llamando a ella misma mientras el valor sea superior a 0
		x = factorial (x , n-1)
		x = x * n
	else:
		x = 1
	return x

try:
	numero = int(input("inserta un numero: "))
    # Ejecutamos la función recusiva para el calculo
	calculo = factorial(1,numero)
	print ("El factorial de %s es %s" % (numero,calculo))
except:
	print ("\nTiene que ser un valor numerico")