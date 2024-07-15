"""
    12. Desarrolle una función que indique si los elementos de la diagonal principal son iguales o no.
"""


def diagonal_principal_igual(matrix):
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("La matriz debe ser cuadrada")

    reference = matrix[0][0]

    for i in range(1, len(matrix)):
        if matrix[i][i] != reference:
            return False

    return True


matrix1 = [[2, 3, 2], [4, 2, 6], [7, 8, 2]]

matrix2 = [[1, 3, 2], [4, 1, 6], [7, 8, 9]]

print(diagonal_principal_igual(matrix1))
print(diagonal_principal_igual(matrix2))
