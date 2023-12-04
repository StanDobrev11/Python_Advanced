"""
1914, September 22 – German submarine U‐9 sinks three unescorted British armored cruisers HMS Aboukir,
HMS Hogue, and HMS Cressy in approximately one hour. Imagine that they had the technology to make themselves a
navigational program for the submarine and you are chosen to implement the logic. Navigate U‐9 through the
battlefield, find and sink the British cruisers in the dark night, avoiding the floating mines all over the North Sea.
You will be given an integer n for the size of the battlefield (square shape). On the next n lines, you will receive the
rows of the battlefield. The submarine will start at a random position, marked with the letter 'S'. The submarine
surveys the surrounding area through its periscope, so it has to climb up to periscope depth, where it might run across
naval mines.
When the submarine receives direction, it goes deep and moves one position toward the given direction. On each
turn, you will be guiding the submarine and giving it the direction, in which it should move. The commands will be
"up", "down", "left" and "right".
When a new position is reached, the submarine climbs up to periscope depth to search for a cruiser:
 If a position with '‐' (dash) is reached, it means that the field is empty and the submarine awaits its next
direction.
 If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown, the position
of the mine will be marked with '‐' (dash). U‐9 can withstand two hits from naval mines. The third time the
submarine is hit by a mine, it disappears and the mission is failed. The battle is over and the following
message should be printed on the Console: "Mission failed, U‐9 disappeared! Last known
coordinates [{row}, {col}]!"
 If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be
marked with '‐' (dash).
 If this is the last (third) battle cruiser on the battlefield, the battle is over and the following message should
be printed on the Console: "Mission accomplished, U‐9 has destroyed all battle cruisers
of the enemy!"
The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three
times).
Input
 On the first line, you are given the integer n – the size of the matrix (wall).
 The next n lines hold the values for every row (NOT separated by anything).
 On each of the next lines you will get a direction command.
Output
 If all battle cruisers are destroyed, print: "Mission accomplished, U‐9 has destroyed all
battle cruisers of the enemy!"
 If U‐9 is hit by a mine three times, print: "Mission failed, U‐9 disappeared! Last known
coordinates [{row}, {col}]!".
 At the end, print the final state of the matrix (battlefield) with the last known U‐9’s position on it.
Constraints
 The size of the square matrix (battlefield) will be between [4…10].
 U‐9’s starting position will always be marked with 'S'.
 There will be always three battle cruisers ‐ fields marked with 'C'.
 There will be always enough mines on the battlefield to destroy the submarine.
 The commands given will direct the submarine only in the limits of the battlefield.
Input       Output
5
*--*-
-S-*C
-*---
-----
-C-*C
right
down
left
up
right
right
right
down
down
down
up
left
left
left
down

            Mission accomplished, U‐9 has destroyed all
            battle cruisers of the enemy!
            *‐‐*‐
            ‐‐‐‐‐
            ‐‐‐‐‐
            ‐‐‐‐‐
            ‐S‐*‐
5
*--*-
-S-*C
-*---
-----
*C-*C
right
right
up
left
left
left
            Mission failed, U‐9 disappeared! Last known
            coordinates [0, 0]!
            S‐‐‐‐
            ‐‐‐‐C
            ‐*‐‐‐
            ‐‐‐‐‐
            *C‐*C
"""


def read_battlefield(n):
    return [[x for x in list(input())] for _ in range(n)]


def print_battlefield():
    for r in battlefield:
        print(''.join(r))


def submarine_position():
    for idx, row in enumerate(battlefield):
        if 'S' in row:
            col = row.index('S')
            row = idx
            return row, col


def move_to_position(course, row, col):
    row += direction_mapper[course][0]
    col += direction_mapper[course][1]
    field = battlefield[row][col]

    try:
        battlefield_mapper[field](row, col)
    except KeyError:
        pass

    return row, col


def destroy_ship(row, col):
    global destroyed_ships
    battlefield[row][col] = '-'
    destroyed_ships += 1


def take_damage(row, col):
    global hits_taken
    battlefield[row][col] = '-'
    hits_taken += 1


def begin_battle():
    row, col = submarine_position()
    battlefield[row][col] = '-'
    while destroyed_ships < 3 and hits_taken < 3:
        course = input()
        row, col = move_to_position(course, row, col)

    battlefield[row][col] = 'S'

    return row, col


def print_outcome(row, col):
    if destroyed_ships >= 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    else:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")


if __name__ == "__main__":
    direction_mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }
    battlefield_mapper = {
        'C': destroy_ship,
        '*': take_damage,
    }
    destroyed_ships = 0
    hits_taken = 0
    battlefield_size = int(input())
    battlefield = read_battlefield(battlefield_size)
    last_row, last_col = begin_battle()
    print_outcome(last_row, last_col)
    print_battlefield()

# def read_matrix(r):
#     matrix = []
#     for _ in range(r):
#         line = list(input())
#         matrix.append(line)
#
#     return matrix
#
#
# def print_matrix(mtrx):
#     for r in mtrx:
#         print(''.join(r))
#
#
# def get_position(mtrx, letter):
#     for row_idx, r in enumerate(mtrx):
#         for col_idx, c in enumerate(r):
#             if mtrx[row_idx][col_idx] == letter:
#                 return row_idx, col_idx
#
#
# def move_sub(mtrx, direction, r, c):
#     global hits_taken
#     global battle_cruisers
#
#     prv_r, prv_c = r, c
#
#     course_mapper = {
#         'up': (r - 1, c),
#         'down': (r + 1, c),
#         'left': (r, c - 1),
#         'right': (r, c + 1)
#     }
#
#     r, c = course_mapper[direction]
#
#     if mtrx[r][c] == '-':
#         mtrx[r][c], mtrx[prv_r][prv_c] = 'S', '-'
#
#     elif mtrx[r][c] == '*':
#         hits_taken += 1
#         mtrx[r][c], mtrx[prv_r][prv_c] = 'S', '-'
#
#     elif mtrx[r][c] == 'C':
#         battle_cruisers -= 1
#         mtrx[r][c], mtrx[prv_r][prv_c] = 'S', '-'
#
#     return r, c
#
#
# rows = int(input())
#
# bfield = read_matrix(rows)
# row, col = get_position(bfield, 'S')
#
# hits_taken = 0
# battle_cruisers = 3
#
# while hits_taken < 3 and battle_cruisers > 0:
#     course = input()
#     row, col = move_sub(bfield, course, row, col)
#
# if hits_taken == 3:
#     print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
# if battle_cruisers == 0:
#     print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#
# print_matrix(bfield)
