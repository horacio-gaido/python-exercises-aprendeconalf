"""
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


"""

investment = float(input("Ingrese la cantidad de dinero que quiere invertir: "))
interest_rate = float(input("Ingrese la tasa anual de interés en porcentaje: "))
years = int(input("Ingrese la cantidad años que quiere invertir: "))
i = 1

for i in range(i,years+1):
    annual_final_capital = (investment * ((1 + ( interest_rate / 100)) ** i))
    print(f"El capital obtenido en el año número {i} es {annual_final_capital:.2f}")

