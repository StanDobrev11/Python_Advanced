"""
Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N
lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You
should start searching from the top left. If there is no such symbol, print the message "{symbol} does not
occur in the matrix".

Input Output
3
ABC
DEF
X!@
!
        (2, 1)
4
asdd
xczc
qwee
qefw
4
        4 does not occur in the matrix
"""


def read_matrix():
    matrix = []
    rows = int(input())
    for _ in range(rows):
        row = list(input())
        matrix.append(row)
    return matrix


matrix = read_matrix()
target_symbol = input()
is_found = False
result = tuple()
for row in matrix:
    if target_symbol in row:
        col = row.index(target_symbol)
        row = matrix.index(row)
        result = (row, col)
        is_found = True
        break

if is_found:
    print(result)
else:
    print(f'{target_symbol} does not occur in the matrix')
