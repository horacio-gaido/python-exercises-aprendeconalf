"""
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
"""
a = 50
divisores_a = []
for i in range(1,a+1):
        if a % i == 0:
            divisores_a.append(i)
divisores_a_set = set(divisores_a)
print(divisores_a_set)

b = 1002
divisores_b = []
for i in range(1,b+1):
        if b % i == 0:
            divisores_b.append(i)
divisores_b_set = set(divisores_b)
print(divisores_b_set)

set_c = divisores_a_set.intersection(divisores_b_set) 
print(set_c)

lista_c = list(set_c)
mcd = lista_c[-1]
print(mcd)