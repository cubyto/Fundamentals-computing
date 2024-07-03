"""
    8. Contar el número de caracteres que hay en un archivo. 
"""


def count_chars():
    with open("./arch_created/lines_interval.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    count_chars = sum(1 for line in lines for chars in line)
    return count_chars


def main():
    num_chars = count_chars()
    print(num_chars)


main()
