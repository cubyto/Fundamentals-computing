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
            if char != " " or char != "\n":
                word += char
            else:
                break
        words.append(word)
    return words


def word_repeat(lista):
    words_repeating = {}
    for word in lista:
        if word in words_repeating:
            words_repeating[word] += 1
        else:
            words_repeating[word] = 1
    countFilter = {k: v for k, v in words_repeating.items() if v > 1}
    return countFilter


def main():
    list_word = word_list()
    num_word = word_repeat(list_word)
    print(num_word)


main()
