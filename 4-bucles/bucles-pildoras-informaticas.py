contador = 0 #Contador en 0

user = input("Ingresa tu correo electronico: ")

for i in user: #Verifica si el valor ingresado contiene el @(arroba) y el .(punto)
    if (i=="@" and i=="@"):
        print("Correo no valido!")
    elif(i=="@" or i=="."): #Condicion donde valida la cantidad de caracteres
        contador = contador+1 #Si cumple con la condicion el contador de incrementa en 1
if contador >= 2: #Si el contador es mayor o igual a 2 manda mensaje
    print("Correo registrado!")
else:
    print("Correo no valido!")

#Asi valida que no acepte el correo con 2 @