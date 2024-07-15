def draw_matrix(m, n):
    matriz = []
    for i in range(m):
        element_rows = []
        if i == 0 or i == m - 1:
            element_rows = ["1"] * n
        else:
            element_rows = ["1" if j == 0 or j == n - 1 else "0" for j in range(n)]
        matriz.append(element_rows)

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
    show_matriz(first_matrix)


main()
