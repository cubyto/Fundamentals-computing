"""
    3. Sumar todos los elementos de una matriz.
"""


def draw_matrix():
    draw_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return draw_matriz


def sum_matrix(matrix):
    sum_matrix = sum(rows[i] for rows in matrix for i in range(len(rows)))
    return sum_matrix


matrix = draw_matrix()
print(matrix)

suma_matrix = sum_matrix(matrix)
print(suma_matrix)
