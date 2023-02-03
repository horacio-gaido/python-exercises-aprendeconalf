"""
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = str(input("Ingrese su nombre: "))
numero_entrero = int(input("Ingrgese un número entero: "))

print((nombre + "\n") * int(numero_entrero))

# for i in range(numero_entrero):
#     print(f"{nombre}")
