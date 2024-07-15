"""
    12. Se tiene el archivo “Dpto_Provincias.txt”, que contiene la cantidad de provincias de cada 
    departamento. El usuario ingresará el nombre de un departamento y el programa debe responder 
    cuántas provincias tiene. En caso que el departamento no esté en el archivo se debe indicar con un 
    mensaje. La estructura del archivo puede ser: 
    Amazonas 7 
    Arequipa 8 
    Huánuco 9 
    Lima 10 
    Tacna 4 
    … 
    
"""


def read_departments(file_path):
    departments = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split()
                department_name = " ".join(parts[:-1])
                province_count = int(parts[-1])
                departments[department_name] = province_count
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    return departments


def get_province_count(departments, department_name):
    if department_name in departments:
        return departments[department_name]
    else:
        return None


def main():
    file_path = "Dpto_Provincias.txt"
    departments = read_departments(file_path)

    user_input = input("Ingrese el nombre del departamento: ")
    province_count = get_province_count(departments, user_input)

    if province_count is not None:
        print(f"El departamento {user_input} tiene {province_count} provincias.")
    else:
        print(f"El departamento {user_input} no se encuentra en el archivo.")


if __name__ == "__main__":
    main()
