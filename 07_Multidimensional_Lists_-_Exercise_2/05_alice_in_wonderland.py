"""
Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you
will receive the rows of the territory:
• Alice will be placed in a random position, marked with the letter "A".
• On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she
collects the tea bags and increases the quantity with the corresponding number.
• There will always be one rabbit hole on the territory marked with the letter "R".
• All of the empty positions will be marked with ".".
After the field state, you will be given commandsfor Alice's movements. Move commands can be: "up", "down", "left"
or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue
collecting. Otherwise, if she steps into the rabbit hole or goes out of the territory, she can't return, and the program
ends.
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
• On the first line, you will be given the integer n – the size of the square matrix
• On the following n lines - matrix representing the field (each position separated by a single space)
• On each of the following lines, you will be given a move command
Output
• On the first line:
o If Alice steps into the rabbit hole or goes out of the territory, print:
"Alice didn't make it to the tea party."
o If she collected at least 10 bags of tea, print:
"She did it! She went to the party."
• On the following lines, print the matrix.
Constraints
• Alice will always either go outside Wonderland or collect 10 bags of tea
• All the commands will be valid
• All of the given numbers will be valid integers in the range [0, 10]

Input       Output
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
            Alice didn't make it to the tea party.
            . * . . 1
            * * * . .
            4 * . 1 .
            . . . 2 .
            . 3 . . .
7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
            She did it! She went to the party.
            * * . 1 1 . .
            * . . . 6 . 5
            * * . R . . .
            . 3 . . 1 . .
            . . . 2 . . 2
            . 3 . . 1 . .
            . 8 3 . . . 2
"""


def read_matrix():
    rows = int(input())
    return [[x for x in input().split()] for _ in range(rows)]


def find_start_psn(mtrx):
    for idx, r in enumerate(mtrx):
        if 'A' in r:
            c = r.index('A')
            r = idx
            return r, c


def is_valid(mtrx, r, c):
    if r not in range(len(mtrx)) or c not in range(len(mtrx)):
        return False
    return True


def is_exit(mtrx, r, c):
    if mtrx[r][c] == 'R':
        mtrx[r][c] = '*'
        return True


def print_matrix(mtrx):
    for r in mtrx:
        print(' '.join(str(x) for x in r))


def make_a_move(mtrx, r, c, tea_collected):
    if is_valid(mtrx, r, c):
        if mtrx[r][c].isdigit():
            tea_collected += int(mtrx[r][c])
            mtrx[r][c] = '*'

    return tea_collected, (r, c)


matrix = read_matrix()
row, col = find_start_psn(matrix)
tea_bags = 0
command = input()
while True:
    matrix[row][col] = '*'
    if command == 'right':
        tea_bags, (row, col) = make_a_move(matrix, row, col + 1, tea_bags)
    elif command == 'left':
        tea_bags, (row, col) = make_a_move(matrix, row, col - 1, tea_bags)
    elif command == 'up':
        tea_bags, (row, col) = make_a_move(matrix, row - 1, col, tea_bags)
    elif command == 'down':
        tea_bags, (row, col) = make_a_move(matrix, row + 1, col, tea_bags)
    if tea_bags >= 10 or not is_valid(matrix, row, col) or is_exit(matrix, row, col):
        break
    command = input()

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
print_matrix(matrix)
