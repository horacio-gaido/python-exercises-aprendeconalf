"""
Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

subjects_list = ["Matemáticas", "Química", "Historia", "Filosofía", "Física", "Contabilidad"]
qualification_list = [10,5,9,8,9,4]

for subject in range(5):
    print(f"En {subjects_list[subject]} has sacado {qualification_list[subject]}")