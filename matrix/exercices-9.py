"""
    7. Sumar dos matrices de MxN.
"""

import random


def draw_matrix(m, n):
    matriz = []
    for i in range(m):
        element_rows = [random.randint(1, 10) for i in range(n)]
        matriz.append(element_rows)

    return matriz


def sum_matrices(f_matrix, s_matrix):
    new_matrix = []
    for i in range(len(f_matrix)):
        sum_elements = [
            f_matrix[i][j] + s_matrix[i][j] for j in range(len(f_matrix[i]))
        ]
        new_matrix.append(sum_elements)
    return new_matrix


data = input(
    "Ingrese la posicion de orden m * n de las matrices que desea generar, separadas por un espacio> "
)
numRows, numCols = map(int, data.split())
first_matrix = draw_matrix(numRows, numCols)
second_matrix = draw_matrix(numRows, numCols)
suma_two_atrices = sum_matrices(first_matrix, second_matrix)
print(first_matrix)
print(second_matrix)
print(suma_two_atrices)
