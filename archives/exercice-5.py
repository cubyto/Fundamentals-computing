"""
    5. Rayuela.txt es un archivo en el cual las líneas se encuentran intercaladas. Crear dos nuevos archivos 
    para guardar la información de forma correcta. 
"""


def interval_lines():
    with open("./arch_created/lines_interval.txt", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if i % 2 != 0:
            with open("./arch_created/pair_lines.txt", "a+") as pair_file:
                pair_file.write(lines[i])
        else:
            with open("./arch_created/odd_lines.txt", "a+") as odd_file:
                odd_file.write(lines[i])


def main():
    interval_lines()


main()
