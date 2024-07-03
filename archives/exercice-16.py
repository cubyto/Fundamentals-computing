def write_archive(input_user):
    with open("./arch_created/texto.txt", "a+") as file_text:
        file_text.write(input_user)
    print(file_text)


def main():
    while True:
        ask_user = input("Usted quiero añadir algo al archivo? responder con si o no> ")
        if ask_user == "si":
            line_user = input("Escriba la linea que desea añadir> ")
            write_archive(line_user)
        else:
            print("Aea ok")
            break


main()
