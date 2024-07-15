def unorder_words():
    file = open("./arch_created/lines_interval.txt", mode="r")
    lines = file.readlines()
    word_list = [line.split() for line in lines]
    print(word_list)
    new_file = open("./arch_created/lines_unorder.txt", mode="w")
    for i in range(1, len(word_list) + 1):
        for j in range(1, len(word_list[i - 1]) + 1):
            if j != len(word_list):
                new_file.write(word_list[-i][-j])
                print(word_list[-i][-j], end=" ")
            else:
                new_file.write("\n")
                print(f"\n")


unorder_words()
