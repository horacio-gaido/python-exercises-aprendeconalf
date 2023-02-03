"""
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""
password1= "contrasena"
password2 = str(input("Ingrese una contrasena: ")).lower()
if password1 == password2:
    print("Has ingresado una contrasena valida.")
else:
    print("Has ingresado una contrasena NO valida.")


