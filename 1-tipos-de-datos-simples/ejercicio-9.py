"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión.

"""
print("")
print("")
print("")
cantidad_invertida = float(input("Ingrese la cantidad de dinero que quiere invertir: "))
tasa_interes = float(input("Tasa de interes de la inversión en formato de porcentaje: "))
cantidad_anos = float(input("Cantidad de años que inverirá: "))
capital_mas_interes = (cantidad_invertida * ((1+(tasa_interes / 100)) ** cantidad_anos))

print(f"Dentro de {cantidad_anos:,.0f} año/s obtendrá un total de $ {capital_mas_interes:,.0f} entre capital e interés por su invesión")
