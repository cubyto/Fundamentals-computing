def draw_matrix():
    draw_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return draw_matriz


def sum_cols(matrix) -> dict:
    sum_cols_dict = {}
    for cols in range(len(matrix)):
        cols_in_row = []
        sum_cols_by_row = 0
        for rows in range(len(matrix)):
            sum_cols_by_row += matrix[rows][cols]
            cols_in_row.append(matrix[rows][cols])
        sum_cols_dict[f"{cols_in_row}"] = sum_cols_by_row
    return sum_cols_dict


def main():
    matrix = draw_matrix()
    sum_all_cols = sum_cols(matrix)
    for k, v in sum_all_cols.items():
        print(f"Suma de la columna {k}: {v}")


main()
