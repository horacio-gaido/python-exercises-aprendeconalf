"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de 
masa corporal calculado redondeado con dos decimales.
"""


peso = float(input("¿Cuánto kilogramos pesas? : "))
estatura = float(input("¿Cuánto metros medis en decimales? : "))
imc = (peso / (estatura ** 2))
imc = round(imc,2)
print (f"Tu índice de masa corporal es {imc}")
