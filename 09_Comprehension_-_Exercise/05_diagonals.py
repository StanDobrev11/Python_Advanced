"""
Using a nested list comprehension, write a program that reads NxN matrix, finds its diagonals,
prints them and their sum as shown below.
Input       Output
3
1, 2, 3
4, 5, 6
7, 8, 9
            First diagonal: 1, 5, 9. Sum: 15
            Second diagonal: 3, 5, 7. Sum: 15
"""


def read_matrix():
    rows = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(rows)]


matrix = read_matrix()

first_diag = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row])) if row == col]
second_diag = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row]) - 1, -1, -1) if
               row + col == len(matrix) - 1]

diagonals = {
    'First diagonal': (first_diag, sum(first_diag)),
    'Second diagonal': (second_diag, sum(second_diag)),
}

# for key, value in diagonals.items():
#     print(f'{key}: {", ".join(map(str, value[0]))}. Sum: {value[1]}')


[print(f'{key}: {", ".join(map(str, value[0]))}. Sum: {value[1]}') for key, value in diagonals.items()]