"""
    5. Hallar la suma de la diagonal principal.
"""


def draw_matrix():
    draw_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return draw_matriz


def sum_diag(matrix) -> dict:
    sum_diag_list = []
    sum_diag_main = 0
    for i in range(len(matrix)):
        sum_diag_main += matrix[i][i]
        sum_diag_list.append(matrix[i][i])
    return {f"{sum_diag_list}": sum_diag_main}


def main():
    matrix = draw_matrix()
    print(matrix)
    sum_all_cols = sum_diag(matrix)
    for k, v in sum_all_cols.items():
        print(f"Suma de la diagonal {k}: {v}")


main()
