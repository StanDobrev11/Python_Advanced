"""
Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
Use nested comprehension for that problem.
Input                   Output
2
1, 2, 3
4, 5, 6
                        [[2], [4, 6]]

4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
                        [[10, 24], [34, 110], [4, 12], []]
"""


def read_matrix():
    rows = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(rows)]


matrix = read_matrix()
matrix = [[num for num in row if num % 2 == 0] for row in matrix]
print(matrix)
