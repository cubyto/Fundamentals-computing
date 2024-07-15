"""
    11. Buscar una palabra en el archivo y reemplazarla por otra 
"""


def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, "r") as file:
        content = file.read()

    new_content = content.replace(old_word, new_word)

    with open(file_path, "w") as file:
        file.write(new_content)

    print(f"Reemplazo completado: '{old_word}' por '{new_word}' en {file_path}")


replace_word_in_file("./arch_created/texto.txt", "linea", "esto")
