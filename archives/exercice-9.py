"""
    9. Contar el número de palabras de un archivo. 
"""


def count_word():
    with open("./arch_created/lines_interval.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    words = []
    for line in lines:
        word = ""
        for char in line:
            if char != " ":
                word += char
            else:
                break
        words.append(word)
    print(words)
    return len(words)


def main():
    num_word = count_word()
    print(num_word)


main()
