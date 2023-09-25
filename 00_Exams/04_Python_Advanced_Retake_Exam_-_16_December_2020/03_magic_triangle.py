"""
Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should
create a magic triangle which follows those rules:
 We start with this simple triangle [[1], [1, 1]]
 We generate the next rows until we reach n amount of rows
 Each number in each row is equal to the sum of the two numbers right above it in the triangle
 If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5

Note: Submit only the function in the judge system
Input
 There will be no inputs
 The function will be tested by passing different values of n
 You can test your function with the test code below
Constraints
 N will be in range [2, 100]

Test Code                               Output
get_magic_triangle(5)
                                        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


# def get_magic_triangle(rows):
#     mtrx = [[1] for _ in range(rows)]
#     for row in range(1, rows):
#         col = row
#         for cur_c in range(1, col + 1):
#             try:
#                 cell = mtrx[row - 1][cur_c] + mtrx[row - 1][cur_c - 1]
#             except IndexError:
#                 cell = 1
#             mtrx[row].append(cell)
#
#     return mtrx


def get_magic_triangle(n):
    mtrx = [[1], [1, 1]]
    for row in range(2, n):
        mtrx.append([1] * (row + 1))
        for col in range(1, row):
            mtrx[row][col] = mtrx[row - 1][col] + mtrx[row - 1][col - 1]

    return mtrx


get_magic_triangle(5)
