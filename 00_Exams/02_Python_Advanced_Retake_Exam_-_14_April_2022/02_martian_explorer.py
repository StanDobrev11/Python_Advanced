"""
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
 One rover ‐ marked with the letter "E"
 Water deposit (one or many) ‐ marked with the letter "W"
 Metal deposit (one or many) ‐ marked with the letter "M"
 Concrete deposit (one or many) ‐ marked with the letter "C"
 Rock (one or many) ‐ marked with the letter "R"
 Empty positions will be marked with "‐"
After that, you will be given the commands for the rover's movement on one line separated by a comma and a space
(", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types
of deposit or a rock:
 When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and
increase its value by 1.
 If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown
below, and the program ends.
 If the rover goes out of the field, it should continue from the opposite side in the same direction. Example:
If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position
(3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
Stop the program if you run out of commands or the rover gets broken.
Input
 On the first 6 lines, you will receive the matrix.
 On the following line, you will receive the commands for the rover separated by a comma and a space.
Output
 For each deposit found while you go through the commands, print out on the console: "{Water, Metal
or Concrete} deposit found at ({row}, {col})"
 If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at
({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
 If the rover has found at least one of each deposit, print on the console: "Area suitable to start
the colony."
 Otherwise, print on the console: "Area not suitable to start the colony."
See examples for more clarification.
Input                           Output
‐ R ‐ ‐ ‐ ‐
‐ ‐ ‐ ‐ ‐ R
‐ E ‐ R ‐ ‐
‐ W ‐ ‐ ‐ ‐
‐ ‐ ‐ C ‐ ‐
M ‐ ‐ ‐ ‐ ‐
down, right, down, right,
down, left, left, left
                                Water deposit found at (3, 1)
                                Concrete deposit found at (4, 3)
                                Metal deposit found at (5, 0)
                                Area suitable to start the colony.
R ‐ ‐ ‐ ‐ ‐
‐ ‐ C ‐ ‐ ‐
‐ ‐ ‐ ‐ M ‐
‐ ‐ W ‐ ‐ ‐
‐ E ‐ W ‐ R
‐ ‐ ‐ ‐ ‐ ‐
up, right, down, right,
right, right
                                Water deposit found at (3, 2)
                                Water deposit found at (4, 3)
                                Rover got broken at (4, 5)
                                Area not suitable to start the colony.
R ‐ ‐ ‐ ‐ ‐
‐ ‐ C ‐ ‐ ‐
‐ ‐ ‐ ‐ M ‐
‐ ‐ W ‐ ‐ ‐
‐ E ‐ W ‐ R
‐ ‐ ‐ ‐ ‐ ‐
up, right, down, right,
right, right
                                Water deposit found at (3, 2)
                                Water deposit found at (4, 3)
                                Rover got broken at (4, 5)
                                Area not suitable to start the colony.
"""
from collections import deque


def read_matrix():
    return [[x for x in input().split(' ')] for _ in range(6)]


def print_matrix(mtrx):
    for row in matrix:
        print(row)


def get_commands():
    return input().split(', ')


def find_start_psn(mtrx):
    for idx, row in enumerate(mtrx):
        if 'E' in row:
            col = row.index('E')
            row = idx
            return row, col


def execute_command(cmds, cur_psn, mtrx, items):
    order = cmds.popleft()
    cur_row, cur_col = cur_psn
    next_row, next_col = cur_psn
    # mapper = {
    #     'up': row - 1,
    #     'down': row + 1,
    #     'left': col - 1,
    #     'right': col + 1,
    # }

    if order == 'up':
        next_row -= 1
    elif order == 'down':
        next_row += 1
    elif order == 'left':
        next_col -= 1
    elif order == 'right':
        next_col += 1

    # checked to be able to pass from the other side/edge of the field where 6 is the size of the matrix
    if next_row not in range(len(mtrx)):
        next_row = 6 - abs(next_row)
    if next_col not in range(len(mtrx[0])):
        next_col = 6 - abs(next_col)
    next_psn = next_row, next_col

    items = check_position(next_psn, mtrx, items)

    mtrx[cur_row][cur_col] = '-'
    mtrx[next_row][next_col] = 'E'

    return next_psn, items


def check_position(psn, mtrx, items={}):
    global is_broken
    r, c = psn
    if mtrx[r][c] == 'W':
        items['W'] += 1
        print(f"Water deposit found at ({r}, {c})")
    if mtrx[r][c] == 'M':
        items['M'] += 1
        print(f"Metal deposit found at ({r}, {c})")
    if mtrx[r][c] == 'C':
        items['C'] += 1
        print(f"Concrete deposit found at ({r}, {c})")

    if mtrx[r][c] == 'R':
        is_broken = True

    return items


def check_materials_quantity(items):
    for value in items.values():
        if value == 0:
            return False
    return True


matrix = read_matrix()
commands = deque(get_commands())
position = find_start_psn(matrix)
is_broken = False
is_area_suitable = False
items = {
    'W': 0,
    'C': 0,
    'M': 0,
}
while commands:
    position, items = execute_command(commands, position, matrix, items)

    if is_broken:
        print(f"Rover got broken at ({position[0]}, {position[1]})")
        break
    if check_materials_quantity(items):
        is_area_suitable = True


if is_area_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
