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


# def valid_move(r, c):
#     if r not in range(len(battle_area)) or c not in range(len(battle_area[0])):
#         return False
#     return True

def valid_move(r, c):
    if r < 0 or r >= size:
        return False
    if c < 0 or c >= size:
        return False

    return True


def make_move(mtrx, pos, direction):
    global armour
    global enemies

    old_r, old_c = pos

    move_mapper = {
        'up': (old_r - 1, old_c),
        'down': (old_r + 1, old_c),
        'left': (old_r, old_c - 1),
        'right': (old_r, old_c + 1),
    }

    if direction not in move_mapper:
        return old_r, old_c

    new_r, new_c = move_mapper[direction]

    if not valid_move(new_r, new_c):
        print_mtrx(mtrx)
        return old_r, old_c

    if mtrx[new_r][new_c] == 'E':  # encounter an enemy
        mtrx[old_r][old_c] = '-'
        mtrx[new_r][new_c] = 'J'
        if enemies > 1:
            armour -= 100
            if armour == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_r}, {new_c}]!")
                print_mtrx(mtrx)
                raise SystemExit
        enemies -= 1

    elif mtrx[new_r][new_c] == 'R':  # repairs
        armour = 300
        mtrx[old_r][old_c] = '-'
        mtrx[new_r][new_c] = 'J'

    else:
        mtrx[old_r][old_c] = '-'
        mtrx[new_r][new_c] = 'J'

    if enemies == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        print_mtrx(mtrx)
        raise SystemExit

    return new_r, new_c


size = int(input())
battle_area = read_mtrx(size)
psn = find_position(battle_area, 'J')

enemies = 4
armour = 300

command = input()
while True:
    psn = make_move(battle_area, psn, command)
    command = input()
