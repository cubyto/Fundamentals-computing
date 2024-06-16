import time


def find_zeros(string, zero_list=None) -> list:
    if zero_list is None:
        zero_list = []

    if "0" not in string:
        return zero_list

    start = None
    end = 0

    for i in range(len(string)):
        if string[i] == "0" and start is None:
            start = i
        elif string[i] != "0" and start is not None:
            end = i
            break
        elif i == len(string) - 1 and start is not None:
            end = i + 1

    if start is not None and end > start:
        zero_list.append(string[start:end])

    if end >= len(string):
        return zero_list

    return find_zeros(string[end:], zero_list)


cadena = "hshshs0023009bvd000vdvd0000000b1bdbsjdjdvsvg00000"
res = find_zeros(cadena)
print(res)
