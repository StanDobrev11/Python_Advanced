"""
You are participating in a Firearm course. It is a training day at the shooting range.
You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by
a single space:
• Your position is marked with the symbol "A"
• Targets marked with the symbol "x"
• All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will receive. The possible
commands are:
• "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
You can only move if the field you want to step on is marked with ".".
• "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position
without moving). Beware that there might be targets that stand in the way of other targets, and you cannot
reach them - you can shoot only the nearest target. When you have shot a target, the field becomes an empty
position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
• If at any point there are no targets left, end the program and print: "Training completed! All
{count_targets} targets hit.".
• If, after you perform all the commands, there are some targets left print: "Training not completed!
{count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
• 5 lines representing the field (symbols, separated by a single space)
• N - count of commands
• On the following N lines - the commands in the format described above
Output
• On the first line, print one of the following:
o If all the targets were shot
"Training completed! All {count_targets} targets hit."
o Otherwise:
 "Training not completed! {count_left_targets} targets left."
• Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the
examples.
Constraints
• All the commands will be valid
• There will always be at least one target
Input               Output
. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1
                    Training not completed! 3 targets left.
                    [4, 1]
. . . . .
. . . . .
. A x . .
. . . . .
. x . . .
2
shoot down
shoot right
                    Training completed! All 2 targets hit.
                    [4, 1]
                    [2, 2]

x . . . .
. . . . .
. . . . .
. . . . .
. . . . A
100
shoot down
move right 2
shoot left
                    Training not completed! 1 targets left.
                    [4, 1]

"""


# def move(mtrx, path, footsteps, cur_r, cur_c):
#     original_r, original_c = cur_r, cur_c
#     if in_range(mtrx, footsteps, path, cur_r, cur_c):
#         is_ok = True
#         for step in range(footsteps):
#             r, c = get_next_position(path, cur_r, cur_c)
#             if not_obstructed(mtrx, r, c):
#                 cur_r, cur_c = r, c
#             else:
#                 is_ok = False
#                 break
#         if is_ok:
#             mtrx[original_r][original_c], mtrx[cur_r][cur_c] = mtrx[cur_r][cur_c], mtrx[original_r][original_c]
#             original_r, original_c = cur_r, cur_c
#     print_matrix(mtrx)
#     return original_r, original_c
# def get_final_move_psn(path, footsteps, r, c):
#     if path == 'right':
#         c += footsteps
#     elif path == 'left':
#         c -= footsteps
#     elif path == 'up':
#         r -= footsteps
#     elif path == 'down':
#         r += footsteps
#
#     return r, c
#
#
# def move(mtrx, path, footsteps, cur_r, cur_c):
#     """
#     This function returns directly the player to the final position if not obstructed. Works together with
#     get final move psn function
#     """
#     if in_range(mtrx, footsteps, path, cur_r, cur_c):
#         r, c = get_final_move_psn(path, footsteps, cur_r, cur_c)
#         if mtrx[r][c] == '.':
#             mtrx[cur_r][cur_c], mtrx[r][c] = mtrx[r][c], mtrx[cur_r][cur_c]
#             cur_r, cur_c = r, c
#     print_matrix(mtrx)
#     return cur_r, cur_c

def read_matrix():
    rows = 5
    return [[x for x in input().split()] for _ in range(rows)]


def print_matrix(mtrx):
    for r in mtrx:
        print(' '.join(str(x) for x in r))


def find_start_psn(mtrx):
    for idx, r in enumerate(mtrx):
        if 'A' in r:
            c = r.index('A')
            r = idx
            return r, c


def get_next_position(path, r, c):
    if path == 'right':
        c += 1
    elif path == 'left':
        c -= 1
    elif path == 'up':
        r -= 1
    elif path == 'down':
        r += 1
    return r, c


def in_boundary(mtrx, r, c):
    if r not in range(len(mtrx)) or c not in range(len(mtrx)):
        return False
    return True


def not_obstructed(mtrx, r, c):
    if mtrx[r][c] == '.':
        return True
    return False


def in_range(mtrx, footsteps, path, r, c):
    if path == 'right':
        c += footsteps
    elif path == 'left':
        c -= footsteps
    elif path == 'up':
        r -= footsteps
    elif path == 'down':
        r += footsteps

    if in_boundary(mtrx, r, c):
        return True
    return False


def move(mtrx, path, footsteps, cur_r, cur_c):
    if in_range(mtrx, footsteps, path, cur_r, cur_c):
        for step in range(footsteps):
            r, c = get_next_position(path, cur_r, cur_c)
            if not_obstructed(mtrx, r, c):
                mtrx[cur_r][cur_c], mtrx[r][c] = mtrx[r][c], mtrx[cur_r][cur_c]
                cur_r, cur_c = r, c
    return cur_r, cur_c


def shoot(mtrx, path, cur_r, cur_c, tgts_shot, tgts_coordinates):
    shot_distance = 4
    for shot in range(1, shot_distance + 1):
        tgt_r, tgt_c = get_next_position(path, cur_r, cur_c)
        if in_boundary(mtrx, tgt_r, tgt_c):
            if not_obstructed(mtrx, tgt_r, tgt_c):
                cur_r, cur_c = tgt_r, tgt_c
                continue
            mtrx[tgt_r][tgt_c] = '.'
            tgts_shot += 1
            tgts_coordinates.append([tgt_r, tgt_c])
            break
    return tgts_shot, tgts_coordinates


def get_targets(mtrx):
    tgt_count = 0
    for r in mtrx:
        tgt_count += r.count('x')
    return tgt_count


matrix = read_matrix()
row, col = find_start_psn(matrix)
initial_targets = get_targets(matrix)
targets_shot = 0
target_coordinates = []
commands = int(input())
for _ in range(commands):
    command, *rest = input().split()
    if command == 'move':
        direction, steps = rest
        row, col = move(matrix, direction, int(steps), row, col)
    elif command == 'shoot':
        direction = rest[0]
        targets_shot, target_coordinates = shoot(matrix, direction, row, col, targets_shot, target_coordinates)
    print_matrix(matrix)
    if targets_shot >= initial_targets:
        print(f"Training completed! All {targets_shot} targets hit.")
        break

if targets_shot < initial_targets:
    print(f"Training not completed! {initial_targets - targets_shot} targets left.")

for lst in target_coordinates:
    print(lst)
