"""
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

"""
numero_1 = float(input("Ingrese un numero: "))
numero_2 = float(input("Ingrese otro numero: "))

if numero_2 == 0:
    print("Se ha generado un error porque el divisor es cero.")
else:
    print(f"{numero_1 / numero_2}")


