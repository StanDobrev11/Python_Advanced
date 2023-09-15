"""
Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example,
the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
Input           Output

2
1, 2, 3
4, 5, 6
                [1, 2, 3, 4, 5, 6]
3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99
                [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]
"""


def read_matrix():
    rows = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(rows)]


matrix = read_matrix()

flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)
