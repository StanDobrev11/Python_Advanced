"""
Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's
rows - N. You will get elements for each column on the following N lines, separated with a single space. You will be
receiving commands in the following format:
• "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
• "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

Input           Output
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
                6 2 3
                4 3 6
                7 8 9
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
                Invalid coordinates
                Invalid coordinates
                Invalid coordinates
                -41 2 3 4
                5 6 7 8
                8 7 6 5
                4 3 2 101
"""


def read_matrix():
    rows = int(input())
    return [[int(x) for x in input().split(' ')] for _ in range(rows)]


def command_input(mtrx):
    command, *rest = input().split()
    while not command == 'END':
        row, col, value = [int(x) for x in rest]
        if check_valid_coordinates(row, col, mtrx):
            if command == 'Add':
                mtrx[row][col] += value
            elif command == 'Subtract':
                mtrx[row][col] -= value
        else:
            print('Invalid coordinates')
        command, *rest = input().split()


def check_valid_coordinates(row, col, mtrx):
    if row not in range(len(mtrx) - 1) or col not in range(len(mtrx[0]) - 1):
        return False
    return True


def print_matrix(mtrx):
    for row in mtrx:
        print(' '.join(str(x) for x in row))


matrix = read_matrix()
command_input(matrix)
print_matrix(matrix)
