"""
You will be given an integer n for the size of the snake territory with square shape. On the next n lines, you will receive
the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'. On random
positions there will be food, marked with '*'. There might also be a lair on the territory. The lair has two burrows.
They are marked with the letter ‐ 'B'. All of the empty positions will be marked with '‐'.
Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with
'.'
Move commands will be: "up", "down", "left", "right".
If the snake moves to a food, it eats the food and increases the food quantity with one.
If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear. If the
snake goes out of its territory, it loses, can't return back and the program ends. The snake needs at least 10 food
quantity to win.
When the snake has gone outside of its territory or has eaten enough food, the game ends.
Input
 On the first line, you are given the integer n – the size of the square matrix.
 The next n lines holds the values for every row.
 On each of the next lines you will get a move command.
Output
 On the first line:
o If the snake goes out of its territory, print: "Game over!"
o If the snake eat enough food, print: "You won! You fed the snake."
 On the second line print all food eaten: "Food eaten: {food quantity}"
 In the end print the matrix.
Constraints
 The size of the square matrix will be between [2…10].
 There will always be 0 or 2 burrows, marked with ‐ 'B'.
 The snake position will be marked with 'S'.
 The snake will always either go outside its territory or eat enough food.
 There will be no case in which the snake will go through itself.
Input       Output          Comments
6
‐‐‐‐‐S
‐‐‐‐B-
‐‐‐‐‐‐
‐‐‐‐‐‐
‐‐B‐‐‐
‐‐*‐‐‐
left
down
down
down
left
            Game over!
            Food eaten: 1
            ‐‐‐‐..
            ‐‐‐‐.‐
            ‐‐‐‐‐‐
            ‐‐‐‐‐‐
            ‐‐.‐‐‐
            ‐‐.‐‐‐
                            1) left 2) down 3) down 5) down
                            ‐‐‐‐S. ‐‐‐‐.. ‐‐‐‐.. ‐‐‐‐..
                            ‐‐‐‐B‐ ‐‐‐‐.‐ ‐‐‐‐.‐ ‐‐‐‐.‐
                            ‐‐‐‐‐‐ ‐‐‐‐‐‐ ‐‐‐‐‐‐ ‐‐‐‐‐‐
                            ‐‐‐‐‐‐ ‐‐‐‐‐‐ ‐‐‐‐‐‐ ‐‐‐‐‐‐
                            ‐‐B‐‐‐ ‐‐S‐‐‐ ‐‐.‐‐‐ ‐‐.‐‐‐
                            ‐‐*‐‐‐ ‐‐*‐‐‐ ‐‐S‐‐‐ ‐‐.‐‐‐
                            3) eat the food: '*' (5, 2)
                            5) the snake goes out from its territory and the
                            program ends
"""


def read_maze():
    size = int(input())
    return [[x for x in list(input())] for _ in range(size)]


def print_maze(maze):
    for r in maze:
        print(''.join(r))


def find_start_psn(board):
    for idx, r in enumerate(board):
        if 'S' in r:
            c = r.index('S')
            r = idx
            return r, c


def get_commands():
    return input().split(', ')


def find_burrows(mtrx):
    for idx, r in enumerate(board):
        if 'B' in r:
            c = r.index('B')
            r = idx
            return r, c


def is_valid(next_psn, mtrx):
    next_r, next_c = next_psn
    if next_r not in range(len(mtrx)) or next_c not in range(len(mtrx[0])):
        return False
    return True


def move_snake(old_psn, next_psn, mtrx, food):
    old_row, old_col = old_psn
    next_row, next_col = next_psn
    if mtrx[next_row][next_col] == 'B':
        mtrx[old_row][old_col] = '.'
        mtrx[next_row][next_col] = 'S'
        b_r, b_c = find_burrows(mtrx)
        old_row, old_col = next_row, next_col
        next_row, next_col = b_r, b_c

    if mtrx[next_row][next_col] == '*':
        food += 1
    mtrx[old_row][old_col] = '.'
    mtrx[next_row][next_col] = 'S'

    next_psn = next_row, next_col
    return next_psn, food


def execute_command(cmds, cur_psn):
    order = cmds
    cur_row, cur_col = cur_psn
    next_row, next_col = cur_psn
    if order == 'up':
        next_row = cur_row - 1
    elif order == 'down':
        next_row = cur_row + 1
    elif order == 'left':
        next_col = cur_col - 1
    elif order == 'right':
        next_col = cur_col + 1

    next_psn = next_row, next_col
    return cur_psn, next_psn


board = read_maze()

next_position = find_start_psn(board)
commands = input()
food = 0
is_out = False
while commands:
    old_position, next_position = execute_command(commands, next_position)
    if is_valid(next_position, board):
        next_position, food = move_snake(old_position, next_position, board, food)
        if food == 10:
            break
    else:
        is_out = True
        row, col = old_position
        board[row][col] = '.'
        break
    commands = input()

if is_out or food < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")
print_maze(board)
