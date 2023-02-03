"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
cada cantidad a dos decimales.


"""
interes = 0.04
try:
    saldo = float (input("Ingrese el saldo de su cuenta de ahorro: "))
    if saldo > 0 :
        a1 = saldo * (1 + interes)
        a2 = saldo * ((1 + interes) ** 2)
        a3 = saldo * ((1 + interes) ** 3)
        print(f"$ {a1:.2f} es la cantidad de dinero ahorrada el primer año")
        print(f"$ {a2:.2f} es la cantidad de dinero ahorrada el segundo año")
        print(f"$ {a3:.2f} es la cantidad de dinero ahorrada el tercer año")
    else:
        print("Ha ingresado un valor incorrecto")
except ValueError:
    print ("Ha ingresado un caracter inválido")
   
