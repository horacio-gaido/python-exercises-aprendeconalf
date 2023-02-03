"""
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.



"""

numero_completo = str(input("Ingrese el precio del producto en euros con dos decimales: "))
entero = numero_completo[:-3]
decimal = numero_completo[-2:]
print(f"El producto vale {entero} euros y {decimal} centésimos de euros")











