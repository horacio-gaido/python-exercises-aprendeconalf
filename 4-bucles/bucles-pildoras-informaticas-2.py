print("Programa de evaluación de direcciones de correo electrónico.")
print()

correo=input("Introduzca un correo electrónico: ")
print()

contador_arroba = 0
contador_punto = 0
contador_incorrecto = 0
validación_arroba = "Falla"
validación_punto = "Falla"
validación_incorrecto = "Falla"

for i in correo:
    if(i=="@"):
        contador_arroba += 1
        if(contador_arroba == 1):
            validación_arroba="Ok"

for i in correo:
    if(i=="."):
        contador_punto += 1
        if(contador_punto >= 1):
            validación_punto="Ok"


for i in correo:
    if i in [" ", "\"", "\'", "(", ")", ",", ":", ";", "<", ">", "[", "\\", "]"]:
        contador_incorrecto += 1
        if(contador_incorrecto == 0):
            validación_incorrecto="Ok"


if contador_arroba == 1 and contador_punto >= 1 and contador_incorrecto == 0:
    print("-> El correo es correcto.")
    print()
    print("Validación de arroba = ", validación_arroba, contador_arroba, "/1")
    print("Validación de puntos = ", validación_punto, contador_punto, ">= 1")
    print("Validación de caracteres no permitidos = ", validación_incorrecto, contador_incorrecto, "/0")

else:
    print("-> El correo NO es correcto.")
    print()
    print("Validación de arroba = ", validación_arroba, contador_arroba, "/1")
    print("Validación de puntos = ", validación_punto, contador_punto, ">= 1")
    print("Validación de caracteres no permitidos = ", validación_incorrecto, contador_incorrecto, "/0")

print()
print("=> Fin del programa.")