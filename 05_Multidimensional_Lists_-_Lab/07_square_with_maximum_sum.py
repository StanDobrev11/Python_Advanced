"""
Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of
its values.
On the first line, you will get matrix sizes in the format "{rows}, {columns}". On the next rows, you will get
elements for each column, separated with a comma and a space ", ".
You should print the found submatrix and the sum of its elements, as shown in the examples

Input               Output
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
                    9 8
                    7 9
                    33
2, 4
10, 11, 12, 13
14, 15, 16, 17
                    12 13
                    16 17
                    58

3, 6
10, 4, 3, 3, 2, 1
8, 8, 5, 6, 8, 6
4, 6, 0, 1, 7, 9
"""


def read_matrix():
    matrix = []
    rows, cols = [int(x) for x in input().split(', ')]
    for _ in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def iter_find_sub_matrix_value(matrix, sub_matrix_values):
    for row in range(len(matrix) - 2):
        for col in range(len(matrix[0]) - 1):
            sub_matrix_value = 0
            sub_matrix = ((matrix[row][col], matrix[row][col + 1]), (matrix[row + 1][col], matrix[row + 1][col + 1]))
            for r in sub_matrix:
                sub_matrix_value += sum(r)
            if sub_matrix_value not in sub_matrix_values:
                sub_matrix_values[sub_matrix_value] = sub_matrix
    return sub_matrix_values


# def recurs_find_sub_matrix_value():
#     if row not in range(len(matrix) - 1) or col not in range(len(matrix[0]) - 1):
#         return
#     current_value = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
#     if current_value not in dict_values:
#         dict_values[current_value] = (
#             (matrix[row][col], matrix[row][col + 1]), (matrix[row + 1][col], matrix[row + 1][col + 1])
#         )
#     recurs_find_sub_matrix_value(row, col + 1, matrix, dict_values)
#     recurs_find_sub_matrix_value(row + 1, col, matrix, dict_values)
#     return dict_values


def find_sum(mtrx, row, col, size):
    if row > len(mtrx) - size[0] and col > len(row) - size[1]:
        return
    current_sum = 0
    current_mtrx = [[None] * size[1] for _ in range(size[0])]
    current_r = 0
    for r in range(row, row + size[0]):
        current_c = 0
        for c in range(col, col + size[1]):
            current_sum += mtrx[r][c]
            current_mtrx[current_r][current_c] = mtrx[r][c]
            current_c += 1
        current_r += 1
    return current_sum, current_mtrx


def recurs_result_matrix(mtrx, results, row, col, size):
    if row not in range(len(mtrx) - 1) or col not in range(len(mtrx[0]) - 1):
        return
    the_sum, the_mtrx = find_sum(mtrx, row, col, size)
    if not results.get(the_sum):
        results[the_sum] = the_mtrx
    recurs_result_matrix(mtrx, results, row + 1, col, size)
    recurs_result_matrix(mtrx, results, row, col + 1, size)
    return results


matrix = read_matrix()

trg_rows = 2
trg_cols = 2
sub_matrix_size = (trg_rows, trg_cols)
result_values = {}

result_values = recurs_result_matrix(matrix, result_values, 0, 0, sub_matrix_size)

matrix_value = max(result_values)
top_matrix = result_values[matrix_value]

for row in top_matrix:
    print(f'{" ".join(map(str, row))}')
print(matrix_value)
