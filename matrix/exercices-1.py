def draw_matrix():
    draw_matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return draw_matriz


def insert_matrix(matrix, i, j):
    num_user = int(
        input(
            f"Que numero desea ingresar en la posicion {i} en i y en {j} en j de la matriz {matrix}: "
        )
    )
    matrix[i][j] = num_user
    return matrix


matrix = draw_matrix()
print(matrix)

data = input(
    "Ingrese la posicion en i y j donde desea hacer un cambio, separado por un espacio> "
)
posI, posJ = map(int, data.split())
new_matrix = insert_matrix(matrix, posI, posJ)
print(new_matrix)
