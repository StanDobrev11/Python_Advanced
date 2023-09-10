"""
Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the
matrix's dimensions in the format "{rows} {columns}". In the following rows, you will receive characters
separated by a single space. Print the number of all square matrices you have found.

Input           Output Comments
3 4
A B B D
E B B B
I J B B
                2
2 2
a b
c d
                0       No 2x2 squares of equal cells exist.
5 4
A A B D
A A B B
I J B B
C C C G
C C K P
                3
"""


def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    return [[x for x in input().split(' ')] for _ in range(rows)]


def get_square_matrix_and_top_left_index(mtrx, row, col, size):
    if row not in range(len(mtrx) - size + 1) or col not in range(len(mtrx[row]) - size + 1):
        return
    current_mtrx = [[None] * size for _ in range(size)]
    current_idx = (row, col)
    current_r = 0
    for r in range(row, row + size):
        current_c = 0
        for c in range(col, col + size):
            current_mtrx[current_r][current_c] = mtrx[r][c]
            current_c += 1
        current_r += 1
    return current_idx, current_mtrx


def get_idx_to_matrix_dictionary(mtrx, size):
    idx_to_mtrx_dict = {}
    for row in range(len(mtrx) - size + 1):
        for col in range(len(mtrx[0]) - size + 1):
            current_idx, current_matrix = get_square_matrix_and_top_left_index(matrix, row, col, SQUARE_SIZE)
            idx_to_mtrx_dict[current_idx] = current_matrix
    return idx_to_mtrx_dict


def get_identical_elements_matrix_count(data):
    count = 0
    for value in data.values():
        test_set = set()
        for row in value:
            for letter in row:
                test_set.add(letter)
        if len(test_set) == 1:
            count += 1
    return count


def print_result(count):
    print(count)


SQUARE_SIZE = 2
matrix = read_matrix()
result_matrix_dictionary = get_idx_to_matrix_dictionary(matrix, SQUARE_SIZE)
count = get_identical_elements_matrix_count(result_matrix_dictionary)
print_result(count)
