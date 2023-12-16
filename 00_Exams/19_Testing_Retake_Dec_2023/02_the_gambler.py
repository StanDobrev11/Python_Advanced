def read_mtrx(n):
    return [list(input()) for _ in range(n)]


def print_mtrx(mtrx):
    for r in mtrx:
        print(''.join(r))


def find_position(mtrx, letter):
    for i_r, r in enumerate(mtrx):
        for i_c, c in enumerate(r):
            if mtrx[i_r][i_c] == letter:
                return i_r, i_c


def valid_move(r, c):
    if r not in range(len(board)) or c not in range(len(board[0])):
        return False
    return True


def make_move(mtrx, pos, direction):
    global cash

    old_r, old_c = pos

    move_mapper = {
        'up': (old_r - 1, old_c),
        'down': (old_r + 1, old_c),
        'left': (old_r, old_c - 1),
        'right': (old_r, old_c + 1),
    }

    new_r, new_c = move_mapper[direction]

    if not valid_move(new_r, new_c):
        print("Game over! You lost everything!")
        raise SystemExit

    if mtrx[new_r][new_c] == 'W':
        mtrx[new_r][new_c] = '-'
        cash += 100

    elif mtrx[new_r][new_c] == 'P':
        cash -= 200

    elif mtrx[new_r][new_c] == 'J':
        cash += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {cash}$")
        mtrx[new_r][new_c] = 'G'
        mtrx[old_r][old_c] = '-'
        print_mtrx(mtrx)
        raise SystemExit

    if cash <= 0:
        print("Game over! You lost everything!")
        raise SystemExit

    mtrx[new_r][new_c] = 'G'
    mtrx[old_r][old_c] = '-'
    return new_r, new_c


size = int(input())

cash = 100

board = read_mtrx(size)
psn = find_position(board, 'G')

command = input()

while command != 'end':
    psn = make_move(board, psn, command)
    command = input()

print(f"End of the game. Total amount: {cash}$")
print_mtrx(board)
