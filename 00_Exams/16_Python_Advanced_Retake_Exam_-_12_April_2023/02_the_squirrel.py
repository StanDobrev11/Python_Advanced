"""
An intern from a big company must solve the game ‐ "The squirrel". He doesn’t have enough experience, so he needs
your help.
Here are the rules of the game:
The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
You get as input the size of the field, which will be always a square shape. After that, you will receive the directions
in which the squirrel can move – "left", "right", "down", and "up" in a sequence, each value separated by a
comma and a space (", "). On the next rows, you will receive the field.
Possible characters in the field:
 s ‐ represents the squirrel's position.
 h – represents a hazelnut.
 * – the asterisk represents an empty position.
 t – represents a trap.
The squirrel starts from the s ‐ position.
 If the squirrel steps on a hazelnut, you have to increase them by 1. The position should be marked with an
asterisk (*).
o If the squirrel collects all 3 hazelnuts, the game ends.
 Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
 If it steps on a trap, the game ends.
 If the squirrel moves out of the field, the game ends.
After all commands you will have 4 possible results:
 You win if the squirrel collects 3 of the hazelnuts.
 The squirrel collects less than 3 hazelnuts.
 The squirrel steps on a trap.
 The squirrel moves out of the field.
Input
 On the first line, you will receive the length of the field – an integer number in the range [3, 5].
 On the second line, you will receive the commands to move the squirrel – an array of strings separated by
", ".
 In the next N lines, you will receive the values for every row.
Output
 On the first line:
o If the squirrel goes out of the field ‐ "The squirrel is out of the field.".
o If the squirrel steps on a trap ‐ "Unfortunately, the squirrel stepped on a trap...".
o If the squirrel hasn’t collected all hazelnuts ‐ "There are more hazelnuts to collect.".
o If the squirrel has collected all hazelnuts ‐ "Good job! You have collected all
hazelnuts!".
 On the second line, print the number of collected hazelnuts ‐ "Hazelnuts collected:
{hazelnutsCount}"
Constraints
 The size of the field will be between [3,5].
 There could be one or no trap on the field.
 There will always be 3 hazelnuts on the field.
Input                   Output
5
left, left, up, right, up, up
**h**
t****
*h***
*h*s*
*****
                        Good job! You have
                        collected all hazelnuts!
                        H azelnuts collected: 3
4
down, down, right, right
*s*h
***h
***t
h ***
                        Unfortunately, the squirrel
                        stepped on a trap...
                        Hazelnuts collected: 0
4
down, down, right, right
h***
***h
*s*t
**h*
                        The squirrel is out of the
                        field.
                        Hazelnuts collected: 0
"""
from collections import deque


def read_field(n):
    return [[x for x in input().split()] for _ in range(n)]


def print_field():
    for row in field:
        print(' '.join(row))


def squirrel_position():
    for idx, row in enumerate(field):
        if 's' in row:
            col = row.index('s')
            row = idx
            return row, col


def valid_position(row, col):
    if row not in range(len(field)) or col not in range(len(field[0])):
        return False
    return True


def move_to_position(course, row, col):
    next_row = row + direction_mapper[course][0]
    next_col = col + direction_mapper[course][1]

    if valid_position(next_row, next_col):
        location = field[next_row][next_col]
    else:
        return row, col

    try:
        field_mapper[location]()
    except KeyError:
        return row, col

    field[row][col] = '-'
    field[next_row][next_col] = 's'
    return next_row, next_col


def start_collecting():
    row, col = squirrel_position()
    while commands:
        next_direction = commands.popleft()
        row, col = move_to_position(next_direction, row, col)

    return print_outcome()


def print_outcome():
    pass


def collect_hazelnut():
    return 1


def free_step():
    pass


def trapped():
    pass


if __name__ == "__main__":
    direction_mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }
    field_mapper = {
        'h': collect_hazelnut,
        '*': free_step,
        't': trapped,
    }
    moves_made = 0
    hazelnuts_collected = 0
    field_rows = int(input())
    commands = deque(x for x in input().split(', '))
    field = read_field(field_rows)
