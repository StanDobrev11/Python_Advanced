"""
Write a program that reads a matrix from the console and performs certain operations with its elements. User input
is provided similarly to the problems above - first, you read the dimensions and then the data.
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1",
"col1") and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the
"swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
    • If the command is valid, you should swap the values at the given indexes and print the matrix at each step
    (thus, you will be able to check if the operation was performed correctly).
    • If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
    or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
    A negative value makes the coordinates not valid.

Your program should finish when the command "END" is entered.

Input           Output
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
                5 2 3
                4 1 6
                Invalid input!
                5 4 3
                2 1 6
1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
                Invalid input!
                World Hello
                Hello World

"""


def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    return [[x for x in input().split(' ')] for _ in range(rows)], (rows, cols)


def check_command_coordinates(cmd, mtrx):
    if len(cmd) != 5:
        return False

    command, *idx = cmd
    if command != 'swap':
        return False
    idx = [int(x) for x in idx]
    for i in idx:
        if i < 0:
            return False
    r_1, c_1, r_2, c_2 = idx
    if (r_1 not in range(len(mtrx)) or
            r_2 not in range(len(mtrx)) or
            c_1 not in range(len(mtrx[0])) or
            c_2 not in range(len(mtrx[0]))):
        return False
    return True


def swap(mtrx, r_1, c_1, r_2, c_2):
    mtrx[r_1][c_1], mtrx[r_2][c_2] = mtrx[r_2][c_2], mtrx[r_1][c_1]


def print_matrix(mtrx):
    for row in mtrx:
        print(' '.join(row))


def command_input(mtrx):
    raw_line = input()
    while raw_line != 'END':
        command = raw_line.split()
        if check_command_coordinates(command, mtrx):
            swap(mtrx, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
            print_matrix(mtrx)
        else:
            print('Invalid input!')
        raw_line = input()


matrix, *rest = read_matrix()
command_input(matrix)
