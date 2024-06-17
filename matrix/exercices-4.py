def draw_matrix():
    draw_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return draw_matriz


def sum_rows(matrix) -> dict:
    sum_rows_dict = {}
    for i in range(len(matrix)):
        sum_col = sum(matrix[i][j] for j in range(len(matrix[i])))
        print(matrix[i])
        sum_rows_dict[f"{matrix[i]}"] = sum_col
    return sum_rows_dict


def main():
    matrix = draw_matrix()
    sum_all_rows = sum_rows(matrix)
    for k, v in sum_all_rows.items():
        print(f"Suma de la fila {k}: {v}")


main()
