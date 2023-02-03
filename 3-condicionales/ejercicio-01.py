"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""

edad = int(input("Decime tu edad: "))
if edad < 0:
    print("Has ingresado una edad no valida")
elif edad > 18:
    print("Eres mayor de edad.")
else: 
    print("Eres menor de edad.")
