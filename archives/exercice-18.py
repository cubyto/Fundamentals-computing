"""
    hayar el promedio de la clase en el 1er examen
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


def avg_first_exam(obj):
    avg_gen = sum(v[0] for _, v in obj.items()) / len(obj)
    return avg_gen


lec = open("./arch_created/database1.txt", "r")
list_student = list_students(lec)
res = avg_first_exam(list_student)
print(res)
