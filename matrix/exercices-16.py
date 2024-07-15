"""
    16. Generar el contenido de las siguientes matrices:
        1 2 3
        4 5 6
        7 8 9
"""


def draw_matrix(m, n):
    matriz = []
    limit = n
    start = 0
    for i in range(m):
        element_rows = [str(i + 1) for i in range(start, limit)]
        limit += n
        start += n
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
