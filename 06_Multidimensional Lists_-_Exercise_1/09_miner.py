"""
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move.
On the second line, you will receive the commands for the miner's movement, separated by a single space. The
possible commands are "left", "right", "up" and "down".
In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the
screen are:
• * - a regular position on the field
• e - the end of the route
• c - coal
• s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving with
only one position in the given direction. If the miner has reached the edge of the field and the following command
indicates that he has to get out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you
should print whether the miner has succeeded in collecting the coal or not and his final position:
• If the miner has collected all coal in the field, the program stops, and you should print the message: "You
collected all coal! ({row_index}, {col_index})".
• If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game
over! ({row_index}, {col_index})".
• If there are no more commands and none of the above cases had happened, you should print the message:
"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
• Field size - an integer number
• Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
• The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
Output
• There are three types of output as mentioned above.
Constraints
• The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
• The field will always have only one "s"
Input                       Output
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *
                            Game over! (1, 3)
4
up right right right down
* * * e
* * c *
* s * c
* * c *
                            You collected all
                            coal! (2, 3)
6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *
                            3 pieces of coal left.
                            (5, 0)

6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *

"""
from collections import deque


def read_matrix():
    dims = int(input())
    cmds = deque(get_commands())
    return [[x for x in input().split(' ')] for _ in range(dims)], cmds


def get_commands():
    return input().split()


def find_start_psn(mtrx):
    for idx, row in enumerate(mtrx):
        if 's' in row:
            col = row.index('s')
            row = idx
            return row, col


def count_coals(mtrx):
    coals = 0
    for row in matrix:
        if 'c' in row:
            coals += row.count('c')
    return coals


def execute_command(cmds, psn, mtrx):
    order = cmds.popleft()
    current_psn = psn
    row, col = current_psn
    if order == 'up':
        row -= 1
    elif order == 'down':
        row += 1
    elif order == 'left':
        col -= 1
    elif order == 'right':
        col += 1
    if row in range(len(mtrx)) and col in range(len(mtrx[0])):
        current_psn = row, col
        return current_psn
    return psn


def collect_coal(psn, mtrx, coal):
    row, col = psn
    cell = mtrx[row][col]
    if cell == 'c':
        coal += 1
        mtrx[row][col] = '*'
        return True, coal
    elif cell == 'e':
        return False, coal
    else:
        return True, coal


def check_and_print(psn, coal, total_coal):
    row, col = psn
    if coal == total_coal:
        print(f"You collected all coal! ({row}, {col})")
        return True
    if not is_playing:
        print(f"Game over! ({row}, {col})")
        return True


matrix, commands = read_matrix()
position = find_start_psn(matrix)
total_coals = count_coals(matrix)
coal_collected = 0
is_over = False
while commands:
    position = execute_command(commands, position, matrix)
    is_playing, coal_collected = collect_coal(position, matrix, coal_collected)
    if check_and_print(position, coal_collected, total_coals):
        is_over = True
        break
if not is_over:
    row, col = position
    print(f'{total_coals - coal_collected} pieces of coal left. ({row}, {col})')
