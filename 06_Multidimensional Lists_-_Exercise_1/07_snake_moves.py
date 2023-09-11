"""
You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end
of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end.
The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's
path is as long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, start
again at the first symbol. In the end, you should print the snake's path.
Input
The input data consists of exactly two lines:
• On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}".
• On the second line, you will receive the string representing the snake
Output
• You should print the snake's zigzag path of size N x M (rows x columns)
Constraints
• The dimensions N and M of the matrix will be integers in the range [1 … 12]
• The snake will be a string with length in the range [1 … 20] and will not contain any whitespace characters

Input   Output

5 6
SoftUni
        SoftUn
        UtfoSi
        niSoft
        foSinU
        tUniSo
1 4
Python
        Pyth
"""
from collections import deque


def create_matrix():
    rows, cols = [int(x) for x in input().split()]
    return [[None] * cols for _ in range(rows)]


def fill_even_row(mtrx, row, snk):
    for col in range(len(mtrx[row])):
        sym = snk.popleft()
        mtrx[row][col] = sym
        snk.append(sym)


def fill_odd_row(mtrx, row, snk):
    for col in range(len(mtrx[row]) - 1, -1, -1):
        sym = snk.popleft()
        mtrx[row][col] = sym
        snk.append(sym)


def fill_matrix(mtrx):
    for row in range(len(mtrx)):
        if row % 2 == 0:
            fill_even_row(mtrx, row, snake)
        else:
            fill_odd_row(mtrx, row, snake)
    return mtrx


def print_matrix(mtrx):
    for row in mtrx:
        print(''.join(row))


matrix = create_matrix()
snake = deque(input())
matrix = fill_matrix(matrix)
print_matrix(matrix)
