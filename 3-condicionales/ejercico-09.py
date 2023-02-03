"""
Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar 5€ 
y si es mayor de 18 años, 10€.


"""

try:
    edad = int(input("¿Cuantos años tenés?: "))
except ValueError:
    print("Ha ingresado una edad incorrecta")

try:
    if edad < 0:
        print("Ha ingresado una edad incorrecta")
    elif edad > 0 and edad < 4:
        print("Podés entrar gratis")
    elif edad >= 4 and edad < 18:
        print("Tenés que pagar 5€")
    elif edad > 18 and edad <= 150:
        print("Tenés que pagar 10€")
    else:
        print("Eres Munra...el inmortal!!!! Bienvenido...podés pasar gratis")
except NameError:
    print("Vuelva a intentarlo")



    