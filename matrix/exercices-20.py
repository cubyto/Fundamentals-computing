def draw_matrix(m, n):
    matriz = []
    for i in range(m):
        element_rows = []
        if i % 2 != 0:
            element_rows = ["1" if j % 2 != 0 else "0" for j in range(n)]
        else:
            element_rows = ["0" if j % 2 != 0 else "1" for j in range(n)]
        matriz.append(element_rows)

    return matriz


def draw_matrix_way2(m, n):
    matriz = [[str((i + j + 1) % 2) for j in range(n)] for i in range(m)]
    return matriz


def show_matriz(matrix: list):
    for rows in range(len(matrix)):
        res = "".join(matrix[rows])
        print(res)


def main():
    data = input(
        "Ingrese la posicion de orden m * n de las matrices que desea generar, separadas por un espacio> "
    )
    numRows, numCols = map(int, data.split())
    first_matrix = draw_matrix(numRows, numCols)
    second_matrix = draw_matrix_way2(numRows, numCols)
    show_matriz(first_matrix)
    show_matriz(second_matrix)


main()
