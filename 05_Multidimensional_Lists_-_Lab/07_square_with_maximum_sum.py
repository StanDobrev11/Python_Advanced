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


def recurs_find_sub_matrix_value(row, col, matrix, dict_values):
    if row not in range(len(matrix) - 1) or col not in range(len(matrix[0]) - 1):
        return
    current_value = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
    if current_value not in dict_values:
        dict_values[current_value] = (
            (matrix[row][col], matrix[row][col + 1]), (matrix[row + 1][col], matrix[row + 1][col + 1])
        )
    recurs_find_sub_matrix_value(row, col + 1, matrix, dict_values)
    recurs_find_sub_matrix_value(row + 1, col, matrix, dict_values)
    return dict_values


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


matrix = read_matrix()

sub_matrix_values = {}
# sub_matrix_values = recurs_find_sub_matrix_value(0, 0, matrix, sub_matrix_values)
sub_matrix_values = iter_find_sub_matrix_value(matrix, sub_matrix_values)

matrix_value = max(sub_matrix_values)
top_matrix = sub_matrix_values[matrix_value]

for row in top_matrix:
    print(f'{" ".join(map(str, row))}')
print(matrix_value)
