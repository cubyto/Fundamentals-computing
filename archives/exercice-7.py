"""
    7. Contar el número de líneas de un archivo. 
"""


def count_lines():
    with open("./arch_created/lines_interval.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    count_lines = sum(1 for line in lines)
    return count_lines


def main():
    num_lines = count_lines()
    print(num_lines)


main()
