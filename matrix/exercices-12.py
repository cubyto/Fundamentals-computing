"""
    11. Desarrolle una función que permita halla el mayor elemento de cada fila, y colocarlos en un
    nuevo vector.
"""


def max_elements_per_row(matrix):
    max_elements = []
    for row in matrix:
        max_elements.append(max(row))
    return max_elements


matrix = [[1, 3, 2], [7, 5, 6], [4, 9, 8]]

result = max_elements_per_row(matrix)
print(result)
