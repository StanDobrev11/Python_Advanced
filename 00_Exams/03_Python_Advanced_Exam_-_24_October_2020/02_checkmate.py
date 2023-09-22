"""
You will be given a chess board (8x8). On the board there will be 3 types of symbols:
 "." – empty square
 "Q" – a queen
 "K" – the king
Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move
diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the
knight). Beware that there might be queens that stand in the way of other queens and can stop them from
capturing the king. For more clarification see the examples.
Input
 8 lines – the state of the board (each square separated by single space)
Output
 The positions of the queens that can capture the king as lists
 If the king cannot be captured, print: "The king is safe!"
 The order of output does not matter
Constrains
 There will always be exactly 8 lines
 There will always be exactly one King
 Only the 3 symbols described above will be present in the input


. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
                    [2, 5]
                    [5, 1]
                    [1, 0]
. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .
                    The king is safe!
Q . . . . . Q .
. . . . . . . .
. . . . . . . .
. . . K . . . .
. . . . . . . .
. . . . . . . .
Q . . . . . . .
. . . . . . . Q
"""


def read_board():
    size = 8
    return [[x for x in input().split()] for _ in range(size)]


def print_result(result):
    if result:
        for item in result:
            print(list(item))
    else:
        print('The king is safe!')


def print_(brd):
    for r in brd:
        print(' '.join(str(x) for x in r))


def find_king(brd):
    for idx, r in enumerate(brd):
        if 'K' in r:
            c = r.index('K')
            r = idx
            psn = r, c
            return psn


def check_attacks(brd, psn, result):
    r, c = psn

    def check_column():
        # check up
        for row in range(r - 1, -1, -1):
            if brd[row][c] == 'Q':
                result.add((row, c))
                break
        # check down
        for row in range(r + 1, 8):
            if brd[row][c] == 'Q':
                result.add((row, c))
                break

    def check_row():
        # check left
        for col in range(c - 1, -1, -1):
            if brd[r][col] == 'Q':
                result.add((r, col))
                break
        for col in range(c + 1, 8):
            if brd[r][col] == 'Q':
                result.add((r, col))
                break

    def check_left_diag():
        diag_value = r - c
        # check top
        for row in range(r - 1, -1, -1):
            is_found = False
            for col in range(c - 1, -1, -1):
                if row - col == diag_value and brd[row][col] == 'Q':
                    result.add((row, col))
                    is_found = True
                    break
            if is_found:
                break
        # check bottom
        for row in range(r + 1, 8):
            is_found = False
            for col in range(c + 1, 8):
                if row - col == diag_value and brd[row][col] == 'Q':
                    result.add((row, col))
                    is_found = True
                    break
            if is_found:
                break

    def check_right_diag():
        diag_value = r + c
        # check top
        for row in range(r - 1, -1, -1):
            is_found = False
            for col in range(c + 1, 8):
                if row + col == diag_value and brd[row][col] == 'Q':
                    result.add((row, col))
                    is_found = True
                    break
            if is_found:
                break
        # check bottom
        for row in range(r + 1, 8):
            is_found = False
            for col in range(c - 1, -1, -1):
                if row + col == diag_value and brd[row][col] == 'Q':
                    result.add((row, col))
                    is_found = True
                    break
            if is_found:
                break

    check_column()
    check_row()
    check_left_diag()
    check_right_diag()
    return result


board = read_board()
position = find_king(board)
queens = check_attacks(board, position, set())
print_result(queens)
