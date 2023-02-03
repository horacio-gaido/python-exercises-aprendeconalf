"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un 
programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del 
paquete que será enviado.



"""
print("")
print("")
print("")

PAYASO = 112
MUNECA = 75


try:
    cant_payaso = int(input("Ingrese la cantidad de payasos que hay en el paquete: "))
except ValueError:
    print ("Ha ingresado una cantidad no entera de payasos")
    cant_payaso = int(input("Ingrese una cantidad entera de payasos que hay en el paquete: "))
try:
    cant_muneca = int(input("Ingrese la cantidad de muñecas que hay en el paquete: "))
except ValueError:
    print ("Ha ingresado una cantidad no entera de muñecas")
    cant_muneca = int(input("Ingrese una cantidad entera de muñecas que hay en el paquete: "))
peso_paquete = (cant_payaso * PAYASO) + (cant_muneca * MUNECA)
print(f"El peso total del paquete enviado es de {peso_paquete} gramos")


