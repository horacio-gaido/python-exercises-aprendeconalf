"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

barras_vendidas = int(input("Ingrese la cantidad de barrras vendidas que no son del día: "))
precio_pan = 3.49
descuento_total = (precio_pan * barras_vendidas) - (barras_vendidas * 0.6) 
descuento = 0.6 
coste_final_total = precio_pan * (1-descuento ) * barras_vendidas 

print (f"El precio habitual sería {precio_pan * barras_vendidas}€ , el descuento que se le hace por no ser fresca es de {descuento_total}€ / ({descuento*100}%) y el coste final total es de {coste_final_total:.2f}€")