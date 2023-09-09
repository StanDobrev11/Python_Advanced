"""
Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example,
the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for
each column separated with a comma and a space ", ".

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
    matrix = []
    rows = int(input())
    for _ in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

result_list = []
# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         result_list.append(matrix[row][col])
for row in matrix:
    result_list.extend(row)

print(result_list)
