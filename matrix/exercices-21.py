def draw_matrix(m, n):
    matriz = []
    matriz.append(["X" if j == 0 or j == n - 1 else " " for j in range(n)])
    start = 0
    limit = n
    for i in range(m - 1):
        element_rows = []
        if i == int(m / 2):
            element_rows = ["X" if j == int(n / 2) else " " for j in range(n)]
        if i < int(m / 2):
            start += 1
            limit -= 1
        else:
            start -= 1
            limit += 1
        element_rows = ["X" if j == start or j == limit - 1 else " " for j in range(n)]
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
