"""
    18. Generar el contenido de las siguientes matrices:
        3 2 1
        2 1 0
        1 0 -1
"""


def draw_matrix(m, n):
    matriz = []
    limit = 0
    start = n
    for i in range(m):
        element_rows = [str(i) for i in range(start, limit, -1)]
        limit -= 1
        start -= 1
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
