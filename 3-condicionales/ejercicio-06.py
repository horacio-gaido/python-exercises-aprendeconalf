"""
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""

nombre = str(input("Ingrese su nombre: ")).lower()
sexo = str(input("Ingrese su sexo: ")).lower()
if sexo == "femenino" and nombre < "m" :
    print ("Usted pertenece al grupo A")
elif sexo == "masculino" and nombre > "o":
    print ("Usted pertenece al grupo A")
else:
    print ("Usted pertenece al grupo B")


    