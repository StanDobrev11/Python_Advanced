"""
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated
by a comma and a space ", ". You should find the matrix's diagonals, prints them, and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}

Input   Output
3
1, 2, 3
4, 5, 6
7, 8, 9
        Primary diagonal: 1, 5, 9. Sum: 15
        Secondary diagonal: 3, 5, 7. Sum: 15
"""


def read_matrix():
    rows = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(rows)]


def get_diagonals(mtrx):
    primary_diagonal = []
    secondary_diagonal = []
    for r in range(len(mtrx)):
        c = (len(mtrx[r]) - 1) - r
        primary_diagonal.append(mtrx[r][r])
        secondary_diagonal.append(mtrx[r][c])
    return primary_diagonal, secondary_diagonal


def calc_sum_both_diagonals(diagonals):
    primary_sum = sum(diagonals[0])
    secondary_sum = sum(diagonals[1])
    return primary_sum, secondary_sum


def print_result(result_lists, result_sums):
    print(f'Primary diagonal: {", ".join(map(str, result_lists[0]))}. Sum: {result_sums[0]}')
    print(f'Secondary diagonal: {", ".join(map(str, result_lists[1]))}. Sum: {result_sums[1]}')


matrix = read_matrix()
diagonals = get_diagonals(matrix)
sums = calc_sum_both_diagonals(diagonals)
print_result(diagonals, sums)
