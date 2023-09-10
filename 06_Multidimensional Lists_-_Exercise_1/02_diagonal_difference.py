"""
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for
each column - N numbers separated by a single space. Print the absolute difference between the primary and the
secondary diagonal sums.

Input       Output      Comments
3
11 2 4
4 5 6
10 8 -12
            15          Primary diagonal: sum = 11 + 5 + (-12) = 4
                        Secondary diagonal: sum = 4 + 5 + 10 = 19
                        Difference: |4 - 19| = 15
4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14
            34
"""


def read_matrix():
    rows = int(input())
    return [[int(x) for x in input().split(' ')] for _ in range(rows)]


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


def find_abs_diagonal_difference(diagonal_sums):
    return abs(diagonal_sums[0] - diagonal_sums[1])


matrix = read_matrix()
diagonals = get_diagonals(matrix)
sums = calc_sum_both_diagonals(diagonals)
print(find_abs_diagonal_difference(sums))
