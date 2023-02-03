"""
Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
subjects_list =[]

while True:
    subjects = str(input("\n\n\nIngrese el nombre de una materia a la cual quiera generar\nun listado y cuando quiera ver el listado escriba el nombre salir:  "))
    subjects_list.append(subjects)
    if subjects == "salir":
        print()
        print(f"A continiación se detalla la lista {subjects_list}")
        break


