"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""
fecha = str(input("Ingrese su fecha de nacimiento con el siguiente formato dd/mm/aaaa: "))
dia = fecha[0:fecha.find("/")]
mes = fecha[fecha.find("/")+1:fecha.rfind("/")]
ano = fecha[6:]
print(f"Usted nació el día {dia} del mes {mes} del año {ano}")












