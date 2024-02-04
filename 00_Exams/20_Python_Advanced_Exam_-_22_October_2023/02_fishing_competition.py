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


def validate_position(mtrx, r, c):
    if r >= len(mtrx):
        r = 0
    if c >= len(mtrx):
        c = 0

    return r, c


def make_move(mtrx, pos, direction):
    global current_catch

    old_r, old_c = pos

    move_mapper = {
        'up': (old_r - 1, old_c),
        'down': (old_r + 1, old_c),
        'left': (old_r, old_c - 1),
        'right': (old_r, old_c + 1),
    }

    new_r, new_c = move_mapper[direction]

    new_r, new_c = validate_position(mtrx, new_r, new_c)

    if mtrx[new_r][new_c] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{new_r},{new_c}]")
        raise SystemExit

    if mtrx[new_r][new_c].isdigit():
        current_catch += int(mtrx[new_r][new_c])
        mtrx[old_r][old_c] = '-'
        mtrx[new_r][new_c] = 'S'

    if mtrx[new_r][new_c] == '-':
        mtrx[old_r][old_c] = '-'
        mtrx[new_r][new_c] = 'S'

    return new_r, new_c

size = int(input())
fishing_area = read_mtrx(size)
psn = find_position(fishing_area, 'S')

target = 20
current_catch = 0
command = input()
while not command == "collect the nets":
    psn = make_move(fishing_area, psn, command)
    command = input()

if current_catch >= target:
    print(f"Success! You managed to reach the quota!\n"
          f"Amount of fish caught: {current_catch} tons.")
    print_mtrx(fishing_area)
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {target - current_catch} tons of fish more.\n"
          f"Amount of fish caught: {current_catch} tons.")
    print_mtrx(fishing_area)