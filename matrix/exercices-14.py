"""
    13. Cree una función que permita encontrar el mayor elemento de la diagonal principal y la
    secundaria.
"""


def max_diagonals(matrix):
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("La matriz debe ser cuadrada")

    n = len(matrix)
    max_principal = matrix[0][0]
    max_secundaria = matrix[0][n - 1]

    for i in range(1, n):
        if matrix[i][i] > max_principal:
            max_principal = matrix[i][i]
        if matrix[i][n - 1 - i] > max_secundaria:
            max_secundaria = matrix[i][n - 1 - i]

    return max_principal, max_secundaria


matrix = [[1, 3, 5], [4, 7, 6], [9, 8, 2]]

max_principal, max_secundaria = max_diagonals(matrix)
print(f"Mayor elemento de la diagonal principal: {max_principal}")
print(f"Mayor elemento de la diagonal secundaria: {max_secundaria}")
