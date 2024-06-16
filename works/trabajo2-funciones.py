"""
Problema 1: Encontrar secuencia de ceros
"""


# Primera forma -> Usando funciones recursivas
def find_zeros_recursive(string, zero_list=None) -> list:
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

    return find_zeros_recursive(string[end:], zero_list)


cadena = "hshshs0023009bvd000vdvd0000000b1bdbsjdjdvsvg00000"
res = find_zeros_recursive(cadena)
print(res)

# Segunda forma -> Iterando sobre la cadena


def render_list_iterating(string) -> list:
    # Lista de operadores y símbolos
    new_str = ""
    for char in string:
        if char != "0":
            new_str += "#"
        else:
            new_str += char
    return new_str.split("#")


def find_zeros_iterating(lista) -> list:
    list_new_var = [zeros for zeros in lista if zeros]
    return list_new_var


cadena = "hshshs0023009bvd000vdvd0000000b1bdbsj0djdvsvg00000"
render_str = render_list_iterating(cadena)
res = find_zeros_iterating(render_str)

print(cadena)
print(res)

# Tercera forma -> Usando expresiones regulares

import re


def find_zeros_regex(string):
    pattern = r"0+"
    list_zeros = re.findall(pattern, string)
    return list_zeros


cadena = "hshshs0023009bvd000vdvd0000000b1bdbsjdjdvsvg00000"

res = find_zeros_regex(cadena)
print(res)

"""Problema 2: encontrar identificadores"""
# Primera forma -> ITerando sobre la cadena

from keyword import kwlist


def render_list(string) -> list:
    # Lista de operadores y símbolos
    operadores_simbolos = "~!@#$%^&*()_+-=,./;[]<>?:{}'|)"
    new_str = ""
    for char in string:
        if char in operadores_simbolos or char == " ":
            new_str += "#"
        else:
            new_str += char
    return new_str.split("#")


def find_new_id(lista: list) -> set:
    list_new_var = {var for var in lista if var and var not in kwlist}
    return list_new_var


cadena = "if num1>num2: mayor=num1"
render_str = render_list(cadena)
res = find_new_id(render_str)
print(res)

# Segunda forma -> Usando expresiones regulares
import re
from keyword import kwlist


def find_new_var(string: str) -> dict:
    pattern = r"\b(\w+)\s{0,1}=\s{0,1}(\d+(\.\d+)?)\b"
    values = re.findall(pattern, string)
    var_val_obj = {
        match[0]: float(match[1]) for match in values if match[0] not in kwlist
    }
    print(var_val_obj)
    return var_val_obj


def main():
    cadena = "if num1=12.23 num2=3.14 mayor= 12 num1>num2: mayor=num1"
    new_values = find_new_var(cadena)
    for k, v in new_values.items():
        print(f"La variable {k} tiene el valor de {v}")


main()
