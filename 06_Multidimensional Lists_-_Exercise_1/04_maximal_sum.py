"""
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its
elements. There will be no case with two or more 3x3 squares with equal maximal sum.
Input
• On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in
the range [1, 20]
• On the following lines, you will receive each row with its columns - integers, separated by a single space in
the range [-20, 20]
Output
• On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
• On the following 3 lines, print each element of the found submatrix, separated by a single space

Input       Output
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
            Sum = 75
            1 4 14
            7 11 2
            8 12 16
5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
            Sum = 34
            2 5 6
            5 4 1
            6 0 5
"""


def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    return [[int(x) for x in input().split(' ')] for _ in range(rows)]


def find_sum(mtrx, row, col, size):
    if row > len(mtrx) - size[0] + 1 or col > len(mtrx[row]) - size[1] + 1:
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
    if row not in range(len(mtrx) - size[0] + 1) or col not in range(len(mtrx[0]) - size[1] + 1):
        return
    the_sum, the_mtrx = find_sum(mtrx, row, col, size)
    if not results.get(the_sum):
        results[the_sum] = the_mtrx
    recurs_result_matrix(mtrx, results, row + 1, col, size)
    recurs_result_matrix(mtrx, results, row, col + 1, size)
    return results


def print_result(data):
    matrix_value = max(data)
    top_matrix = data[matrix_value]
    print(f"Sum = {matrix_value}")
    for row in top_matrix:
        print(f'{" ".join(map(str, row))}')


matrix = read_matrix()

trg_rows = 3
trg_cols = 3
sub_matrix_size = (trg_rows, trg_cols)
result_values = {}

result_values = recurs_result_matrix(matrix, result_values, 0, 0, sub_matrix_size)
print_result(result_values)
