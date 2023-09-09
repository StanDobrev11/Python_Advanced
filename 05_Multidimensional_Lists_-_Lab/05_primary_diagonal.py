"""
Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom
right). On the first line, you will receive an integer N – the size of a square matrix. The next N lines hold the values
for each column - N numbers, separated by a single space.

Input       Output
3
11 2 4
4 5 6
10 8 -12
            4
3
1 2 3
4 5 6
7 8 9
            15
"""


def read_matrix():
    matrix = []
    rows = int(input())
    for _ in range(rows):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

diag_sum = 0
for row in range(len(matrix)):
    col = row
    diag_sum += matrix[row][col]

print(diag_sum)

diag_sum = 0
col = len(matrix) - 1
for row in range(len(matrix)):
    diag_sum += matrix[row][col]
    col -= 1

print(diag_sum)
