"""
Ejercicio 8
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
"""
import statistics 

lista = [1,2,3,4,5,6,7,8,9,10]

def dict_information (lista):
    media = statistics.mean(lista)
    varianza = statistics.variance(lista)
    des_tipica = statistics.stdev(lista)
    return media, varianza , des_tipica

key_results = ("media", "varianza" , "des_tipica")
results = dict_information (lista)

#using zip() and dict()  
abtract = dict(zip(key_results, results))  
#displaying the resultant dictionary  
print("The resultant dictionary is: ", abtract)  
