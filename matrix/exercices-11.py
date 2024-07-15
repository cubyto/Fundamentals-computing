"""
    9. Indicar si una matriz es identidad o no lo es.
"""


def draw_matrix(m, n):
    matriz = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
    return matriz


def check_matrix_id(f_matrix):
    status = False
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[i])):
            status = (
                True
                if (i == j and f_matrix[i][j] == 1) or (i != j and f_matrix[i][j] == 0)
                else False
            )

    return status


data = input(
    "Ingrese la posicion de orden m * n de las matrices que desea generar, separadas por un espacio> "
)
numRows, numCols = map(int, data.split())
first_matrix = draw_matrix(numRows, numCols)
chg_matrix = check_matrix_id(first_matrix)
print(first_matrix)
print(chg_matrix)
