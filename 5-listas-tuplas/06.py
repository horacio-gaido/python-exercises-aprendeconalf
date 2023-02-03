"""
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y 
elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

subjects_list =["Matemáticas", "Química", "Historia", "Filosofía", "Física", "Contabilidad"]
approved_subjects = []

for subjects in subjects_list:
    qualification = float(input(f"Que no ta ha sacado en {subjects}: "))
    if qualification >= 4:
        approved_subjects.append(subjects)

for subjects in approved_subjects:
    subjects_list.remove(subjects)
print (f"Tienes que repetir las siguientes materias: {subjects_list}")




