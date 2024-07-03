"""
    10. Contar cuantas veces se repite una palabra en un archivo. 
"""


def word_list():
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
    return words


def word_repeat(lista):
    words_repeating = {}


def main():
    num_word = count_word()
    print(num_word)


main()
