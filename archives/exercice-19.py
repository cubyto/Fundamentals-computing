"""
    Hallar el promedio mas alto
"""


def list_students(lec):
    alumnos_obj = {}
    for linea in lec:
        alumnos = linea.split(":")
        alumnos_obj[alumnos[0]] = [
            int(alumnos[i].rstrip()) for i in range(1, len(alumnos))
        ]
    lec.close()
    return alumnos_obj


def avg_max(obj):
    nota_max = max()


lec = open("./arch_created/database1.txt", "r")
list_student = list_students(lec)
