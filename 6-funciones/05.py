"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
area = pi .radio ** 2 
volumen = (pi* radio ** 2) * altura

"""
import math

def area_circulo (radio):
    volumen = radio ** 2 * math.pi
    return volumen

def volumen_cilindro (altura, area_circulo):
    vol_cilindro = altura * area_circulo
    return vol_cilindro

print(volumen_cilindro (5,area_circulo(3)))
