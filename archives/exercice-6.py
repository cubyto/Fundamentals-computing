"""
    6. Leer cadenas desde teclado y copiarlas en un archivo, el programa debe detenerse cuando se ingresa 
    una línea en blanco. 
"""


def write_archive():
    while True:
        line_user = input(
            "Ingrese lo que desea añadir al archivo, se detiene si no ingresa caracter alguno"
        )
        if line_user != "":
            with open(
                "./arch_created/new_archive.txt", "a+", encoding="utf-8"
            ) as new_file:
                new_file.write(f"{line_user} \n")
        else:
            break


write_archive()
