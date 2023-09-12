"""
Chess is the oldest game, but it is still popular these days. You will use only one
chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated. It can move to
the nearest square but not on the same row, column, or diagonal. (e.g., it can
move two squares horizontally, then one square vertically, or it can move one
square horizontally then two squares vertically - i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. Your task
is to remove knights until no knights that can attack one another with one
move are left.
Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the
same number of attacks, remove the top-left one.
Input
• On the first line, you will receive integer N - the size of the board
• On the following N lines, you will receive strings with "K" and "0"
Output
• Print a single integer with the number of knights that need to be removed.
Constraints
• The size of the board will be 0 < N < 30
• Time limit: 0.3 sec. Memory limit: 16 MB
Input   Output
5
0K0K0
K000K
00K00
K000K
0K0K0
        1
2
KK
KK
        0
8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
        12
5
K0000K
00K000
K000K0
00K000
K000K0
"""


def read_board():
    rows = int(input())
    mtrx = []
    for _ in range(rows):
        line = list(input())
        for idx, symbol in enumerate(line):
            if symbol.isdigit():
                line[idx] = int(symbol)
        mtrx.append(line)
    return mtrx


def print_board(board):
    for row in board:
        print(''.join(str(x) for x in row))


def get_key_by_value(val, dct):
    for key, value in dct.items():
        if val == value:
            return key


def return_tgt_squares(row, col):
    tgt_row = range(row - 2, row + 3)
    tgt_col = range(col - 2, col + 3)
    left_diag = col + row
    right_diag = col - row
    return tgt_row, tgt_col, left_diag, right_diag


def increase_tgt_squares(board, cur_row, cur_col):
    tgt_row, tgt_col, left_diag, right_diag = return_tgt_squares(cur_row, cur_col)
    for r in tgt_row:
        if r not in range(len(board)) or r == cur_row:
            continue
        for c in tgt_col:
            if c == cur_col or c not in range(len(board[0])):
                continue
            if (c + r) == left_diag or (c - r) == right_diag:
                continue
            if board[r][c] != 0:
                board[cur_row][cur_col] += 1


def reduce_tgt_squares(board, cur_row, cur_col):
    tgt_row, tgt_col, left_diag, right_diag = return_tgt_squares(cur_row, cur_col)
    for r in tgt_row:
        if r not in range(len(board)) or r == cur_row:
            continue
        for c in tgt_col:
            if c == cur_col or c not in range(len(board[0])):
                continue
            if (c + r) == left_diag or (c - r) == right_diag:
                continue
            if board[r][c] > 0:
                board[r][c] -= 1
                board[cur_row][cur_col] -= 1


def get_max_attack_and_coordinates(board):
    max_value = 0
    max_idx = ()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > max_value:
                max_value = board[row][col]
                max_idx = (row, col)
    if max_value == 0:
        return False
    return max_value, max_idx


def transform_board(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'K':
                board[row][col] = 0
                increase_tgt_squares(board, row, col)


def find_knights_count(board):
    knights_count = 0
    attack_coordinates = get_max_attack_and_coordinates(board)
    while attack_coordinates:
        attack, (row, col) = attack_coordinates
        reduce_tgt_squares(board, row, col)
        knights_count += 1
        attack_coordinates = get_max_attack_and_coordinates(board)
    return knights_count


matrix = read_board()
transform_board(matrix)
print(find_knights_count(matrix))
