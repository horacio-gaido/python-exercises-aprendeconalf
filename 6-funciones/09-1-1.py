"""
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
"""
a = 42
divisores_a = []
for i in range(1,a+1):
        if a % i == 0:
            divisores_a.append(i)
print(divisores_a)

b = 48
divisores_b = []
for i in range(1,b+1):
        if b % i == 0:
            divisores_b.append(i)
print(divisores_b)