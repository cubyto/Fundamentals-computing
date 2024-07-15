"""
    8. Intercambiar la fila X con la fila Y.
"""

import random


def draw_matrix(m, n):
    matriz = []
    for i in range(m):
        element_rows = [random.randint(1, 10) for i in range(n)]
        matriz.append(element_rows)

    return matriz


def change_row(f_matrix, rowInit, rowFin):
    new_matrix = f_matrix
    print(len(new_matrix))
    new_matrix[rowInit - 1], new_matrix[rowFin - 1] = (
        new_matrix[rowFin - 1],
        new_matrix[rowInit - 1],
    )
    return new_matrix


data_matrix = input(
    "Ingrese la posicion de orden m * n de las matrices que desea generar, separadas por un espacio> "
)
numRows, numCols = map(int, data_matrix.split())
first_matrix = draw_matrix(numRows, numCols)
print(first_matrix)
data_to_change = input(
    "Ingrese la posicion de las filas que quiere intercambiar de lugar, separadas por un espacio> "
)
rowX, rowY = map(int, data_to_change.split())

chg_matrix = change_row(first_matrix, rowX, rowY)
print(chg_matrix)
