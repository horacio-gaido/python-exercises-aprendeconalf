"""
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.


"""

try:
    renta_anual = float(input("¿Cuánto es su renta anual?: "))
except ValueError:
    print("Ha ingresado un monto de renta anual inválido")

try:
    if renta_anual < 0:
        print("Ha ingresado un monto de renta anual inválido")
    elif renta_anual > 0 and renta_anual < 10000:
        print("Su tipo impositivo es del 5%.")
    elif renta_anual >= 10000 and renta_anual <= 20000:
        print("Su tipo impositivo es del 15%.")
    elif renta_anual > 20001 and renta_anual <= 35000:
        print("Su tipo impositivo es del 20%.")
    elif renta_anual > 35001 and renta_anual <= 60000:
        print("Su tipo impositivo es del 30%.")
    elif renta_anual > 60000:
        print("Su tipo impositivo es del 45%.")
except NameError:
    print("Vuelva a intentarlo")

    