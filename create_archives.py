import os
import re

import fitz


def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def get_exercices(text):
    pattern = r"^\d+\.\s"
    exercices = []
    for i in range(len(text)):
        if re.match(pattern, text[i]):
            exercice = [text[i]]
            for j in range(i + 1, len(text)):
                if not re.match(pattern, text[j]):
                    exercice.append(text[j])
                else:
                    break
            exercices.append(exercice)
    return [exercice for exercice in exercices if exercice or exercice != " "]


def read_file(pdf_path):
    pdf_file = fitz.open(pdf_path)
    complete_list = []
    for page_num in range(len(pdf_file)):
        page_file = pdf_file.load_page(page_num)
        text_file = page_file.get_text("text")
        complete_list += get_exercices(text_file.split("\n"))
    return complete_list


def create_python_files(dir_name, pdf_path):
    list_exercices = read_file(pdf_path)
    for i in range(len(list_exercices)):
        file_name = f"exercice-{i+1}.py"
        file_path = os.path.join(dir_name, file_name)

        with open(file_path, "w", encoding="utf-8") as file_py:
            file_py.write("'''\n")
            for line in list_exercices[i]:
                if line != " ":
                    file_py.write(f"    {line}\n")
            file_py.write("'''\n")
    return len(list_exercices)


def main():
    dir_name = input("Ingrese el nombre que quiere dar a la carpeta> ")
    pdf_name = input("INgrese el nombre en donde se encuentra sus ejercicios> ")
    pdf_path = f"./../{pdf_name}"

    create_directory(dir_name)
    files_created = create_python_files(dir_name, pdf_path)
    print(
        f"Se creo la carpeta {dir_name} y dentro se añadieron {files_created} archivos"
    )


main()
