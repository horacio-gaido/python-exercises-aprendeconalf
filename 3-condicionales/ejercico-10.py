"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

"""

vegetariana = 1
no_vegetariana = 2

try:
    pregunta_1 = int(input("Presione el número '1' si quiere una pizza vegetariana y el '2' si quiere una pizza NO vegetariana: "))
except ValueError:
    print("Ha ingresado un número de opción inválido.")
try:
    if pregunta_1 == 1:
        print("Los ingredientes disponibles para que elija son: pimiento o tofu, sólo puede elegir un ingrediente.")
        pregunta_2 = int(input("Presione el número '3' si quiere la pizza con pimiento o '4' si quiere la pizza con tofu, además de la mozzarella y el tomate que están en todas la pizzas : "))
        if pregunta_2 == 3:
                print("La pizza que eligió es vegetariana y lleva como ingredientes mozzarella, tomate y pimiento.")
        elif pregunta_2 == 4:
            print("La pizza que eligió es vegetariana y lleva como ingredientes mozzarella, tomate y tofu.")
        else:
            print("Ha elegido una opción inválida")

    elif pregunta_1 == 2:
        print("Los ingredientes disponibles para que elija son: peperoni, jamón y salmón, sólo puede elegir un ingrediente.")
        pregunta_3 = int(input("Presione el número '5' si quiere la pizza con peperoni o '6' si quiere la pizza con jamón o '7' si quiere la pizza con salmón además de la mozzarella y el tomate que están en todas la pizzas : "))
        if pregunta_3 == 5:
                print("La pizza que eligió NO es vegetariana y lleva como ingredientes mozzarella, tomate y peperoni.")
        elif pregunta_3 == 6:
            print("La pizza que eligió NO es vegetariana y lleva como ingredientes mozzarella, tomate y jamón.")
        elif pregunta_3 == 7:
            print("La pizza que eligió NO es vegetariana y lleva como ingredientes mozzarella, tomate y salmón.")
        else:
            print("Ha elegido una opción inválida")
    else:
        print("Ha elegido una opción inválida")
except NameError:
    print("Vuelva a intentarlo")