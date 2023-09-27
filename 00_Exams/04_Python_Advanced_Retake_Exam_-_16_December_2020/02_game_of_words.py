"""
You will be given a string. Then, you will be given an integer N for the size of the field with square shape. On the
next N lines, you will receive the rows of the field. The player will be placed on a random position, marked with "P".
On random positions there will be letters. All of the empty positions will be marked with "‐".
Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it,
concatеnates it to the initial string and the letter disappears from the field. If he tries to move outside of the field,
he is punished ‐ he loses the last letter in the string, if there are any, and the player’s position is not changed.
At the end print all letters and the field.
Input
 On the first line, you are given the initial string
 On the second line, you are given the integer N ‐ the size of the square matrix
 The next N lines holds the values for every row
 On the next line you receive a number M
 On the next M lines you will get a move command
Output
 On the first line the final state of the string
 In the end print the matrix
Constraints
 The size of the square matrix will be between [2…10]
 The player position will be marked with "P"
 The letters on the field will be any letter except for "P"
 Move commands will be: "up", "down", "left", "right"

Input                   Output                  Comments
Hello
4
P‐‐‐
Mark
‐l‐y
‐‐e‐
4
down
right
right
right
                        HelloMark
                        ‐‐‐‐
                        ‐‐‐P
                        ‐l‐y
                        ‐‐e‐
                                                The initial string we receive is "Hello". Then we
                                                receive 4x4 field and the player is on index [0;0].
                                                Then, we start receiving commands. First the player
                                                moves to [1;0], where he consumes 'M', and then all
                                                letters on the right. Оur string is "HelloMark" and
                                                the player is on index [1;3].
Initial
5
‐‐‐‐‐
t‐r‐‐
‐‐Pa‐
‐‐S‐‐
z‐‐t‐
4
up
left
left
left
                        Initialr
                        ‐‐‐‐‐
                        P‐‐‐‐
                        ‐‐‐a‐
                        ‐‐S‐‐
                        z‐‐t‐
                                                The initial string we receive is "Initial". Then we
                                                receive 5x5 field and the player is on index [2;2].
                                                The player consumes 'r' and 't', but also tries to go
                                                out of the matrix once, so he loses the last character
                                                of his string – 't'.
"""


def read_matrix():
    rows = int(input())
    return [[x for x in list(input())] for _ in range(rows)]


def print_(mtrx):
    for r in mtrx:
        print(''.join(str(x) for x in r))


def start_psn(mtrx):
    for idx, r in enumerate(mtrx):
        if 'P' in r:
            c = r.index('P')
            r = idx
            return r, c


def is_valid(mtrx, next_psn):
    r, c = next_psn
    if r not in range(len(mtrx)) or c not in range(len(mtrx)):
        return False
    return True


def move_player(cmd, mtrx, cur_row, cur_col, text):

    move_mapper = {
        'left': (cur_row, cur_col - 1),
        'right': (cur_row, cur_col + 1),
        'up': (cur_row - 1, cur_col),
        'down': (cur_row + 1, cur_col),
    }

    if not is_valid(mtrx, move_mapper[cmd]):
        text = text[:-1]
        return cur_row, cur_col, text

    next_r, next_c = move_mapper[cmd]
    if mtrx[next_r][next_c].isalpha():
        text += mtrx[next_r][next_c]

    mtrx[next_r][next_c] = 'P'
    mtrx[cur_row][cur_col] = '-'

    return next_r, next_c, text


string = input()
matrix = read_matrix()
row, col = start_psn(matrix)
commands_count = int(input())

for _ in range(commands_count):
    command = input()
    row, col, string = move_player(command, matrix, row, col, string)
print(string)
print_(matrix)
