def print_(mtrx):
    for row in mtrx:
        print(' '.join(map(str, row)))


def place_coin(mtrx, col, player, row=0):
    mark = 'X' if player == 1 else 'O'
    if row >= ROWS or mtrx[row][col] != '.':
        mtrx[row - 1][col] = mark
        return
    if mtrx[row][col] == '.':
        place_coin(mtrx, col, player, row + 1)


def get_turn(player):
    return 1 if player == 2 else 2


def win(mtrx, col, row=0):
    def check_horizontals():
        horizontal_count = 1
        for c in range(col - 1, -1, -1):
            if c < 0 or mtrx[row][c] != mark:
                break
            horizontal_count += 1
        for c in range(col + 1, COLS):
            if c >= COLS or mtrx[row][c] != mark:
                break
            horizontal_count += 1
        return True if horizontal_count >= 4 else False

    def check_verticals():
        vertical_count = 1
        for r in range(row - 1, -1, -1):
            if r < 0 or mtrx[r][col] != mark:
                break
            vertical_count += 1
        for r in range(row + 1, ROWS):
            if r >= ROWS or mtrx[r][col] != mark:
                break
            vertical_count += 1
        return True if vertical_count >= 4 else False

    def check_left_diagonal():  # row - col
        left_count = 1
        left_diag_key = row - col
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if r - c == left_diag_key:
                    if r < 0 or c < 0 or mtrx[r][c] != mark:
                        break
                    left_count += 1
        for r in range(row + 1, ROWS):
            for c in range(col + 1, COLS):
                if r - c == left_diag_key:
                    if r >= ROWS or c >= COLS or mtrx[r][c] != mark:
                        break
                    left_count += 1
        return True if left_count >= 4 else False

    def check_right_diagonal():
        right_count = 1
        right_diag_key = row + col
        for r in range(row - 1, -1, -1):
            for c in range(col + 1, COLS):
                if r + c == right_diag_key:
                    if r >= ROWS or c >= COLS or mtrx[r][c] != mark:
                        break
                    right_count += 1
        for r in range(row + 1, ROWS):
            for c in range(col - 1, -1, -1):
                if r + c == right_diag_key:
                    if r < 0 or c < 0 or mtrx[r][c] != mark:
                        break
                    right_count += 1
        return True if right_count >= 4 else False

    for row in range(ROWS):
        if mtrx[row][col] != '.':
            break
    mark = mtrx[row][col]
    if (check_horizontals() or
            check_verticals() or
            check_left_diagonal() or
            check_right_diagonal()):
        return True


def is_valid(col):
    if col - 1 not in range(COLS):
        return False
    return True


ROWS, COLS = 6, 7
matrix = [['.'] * COLS for _ in range(ROWS)]

player = 1
while True:
    print_(matrix)

    column = int(input(f'Current player {player} -> choose col: '))
    while True:
        if not is_valid(column):
            print('Not valid column')
            column = int(input(f'Current player {player} -> choose col: '))
        else:
            break

    column -= 1
    place_coin(matrix, column, player)
    if win(matrix, column):
        print(f'Winner is Player {player}')
        print_(matrix)
        break
    player = get_turn(player)
    print()
