"""
5
0K0K0
K000K
00K00
K000K
0K0K0
"""


def read_board():
    rows = int(input())
    return [list(input()) for _ in range(rows)]


def boundaries(board, row, col):
    if row in range(len(board)) and col in range(len(board)):
        return True
    return False


def calculate_attacks(board, row, col):
    tgt_coor = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    attacks = 0
    for coor in tgt_coor:
        tgt_row, tgt_col = coor
        tgt_row += row
        tgt_col += col
        if boundaries(board, tgt_row, tgt_col):
            if board[tgt_row][tgt_col] == 'K':
                attacks += 1
    return attacks


def find_max_attack(board):
    max_attack = 0
    max_attack_coor = ()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'K':
                attacks = calculate_attacks(board, row, col)
                if attacks > max_attack:
                    max_attack = attacks
                    max_attack_coor = (row, col)
    return max_attack, max_attack_coor


def remove_knight(board, removed):
    max_attack, max_coor = find_max_attack(board)
    if max_attack == 0:
        print(removed)
        return
    max_row, max_col = max_coor
    board[max_row][max_col] = '0'
    removed += 1
    return remove_knight(board, removed)


matrix = read_board()
remove_knight(matrix, 0)
