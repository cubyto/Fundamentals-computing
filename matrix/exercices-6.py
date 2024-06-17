def draw_matrix(m, n):
    draw_matriz = [[0] * n for i in range(m)]
    return draw_matriz


data = input(
    "Ingrese la posicion de orden m * n de la matriz que desea dibujar, separadas por un espacio> "
)
numRows, numCols = map(int, data.split())
new_matrix = draw_matrix(numRows, numCols)
print(new_matrix)
