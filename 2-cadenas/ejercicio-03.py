"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

nombre = str(input("Ingrese su nombre: "))
nombre = nombre.upper()
nombre_limpio = nombre.replace(' ', '')
n = len(nombre_limpio)


print(f"{nombre} tiene {n} letras")

