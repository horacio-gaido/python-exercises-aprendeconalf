"""
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

"""
def monto_iva_incluido(monto_neto, iva=0.21):
    monto_total = monto_neto * (1 + iva)
    return monto_total

print(monto_iva_incluido(1000,0.10))
print(monto_iva_incluido(1000))