"""
    Hallar el promedio de cada alumno
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


def promedio(obj):
    for k, v in list_student.items():
        avg = sum(v) / len(v)
        print(f"Alumno => {k}, promedio => {avg}")


lec = open("./arch_created/database1.txt", "r")
list_student = list_students(lec)
promedio(list_student)
