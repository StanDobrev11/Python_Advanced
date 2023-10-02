"""
You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop
represented as some symbols separated by a single space:
 Your position is marked with the symbol "Y"
 Christmas decorations are marked with the symbol "D"
 Gifts are marked with the symbol "G"
 Cookies are marked with the symbol "C"
 All of the empty positions will be marked with "."
After the field state, you will be given commands until you receive the command "End". The commands will be in
the format "right/left/up/down‐{steps}". You should move in the given direction with the given steps and
collect all the items that come across. If you go out of the field, you should continue to traverse the field from the
opposite side in the same direction. You should mark your path with "x". Your current position should always be
marked with "Y".
Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry
Christmas!".
Input
 On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
 On the next lines, you will receive each row with its columns ‐ symbols, separated by a single space.
 On the following lines, you will receive commands in the format described above until you receive the
command "End" or until you collect all items.
Output
 On the first line, if you have collected all items, print:
o "Merry Christmas!"
o Otherwise, skip the line
 Next, print the number of collected items in the format:
o "You've collected:
o ‐ {number_of_decoration} Christmas decorations
o ‐ {number_of_gifts} Gifts
o ‐ {number_of_cookies} Cookies"
 Finally, print the field, as shown in the examples.
Constrains
 All the commands will be valid
 There will always be at least one item
 The dimensions of the matrix will be integers in the range [1, 20]
 The field will always have only one "Y"
 On the field, there will always be only the symbols shown above.
Input           Output
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End
                You've collected:
                ‐ 2 Christmas decorations
                ‐ 1 Gifts
                ‐ 0 Cookies
                . . . . .
                C . . G .
                . C . . .
                G . Y C .
                x x x x x
                x . x x x
5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3
                Merry Christmas!
                You've collected:
                ‐ 2 Christmas decorations
                ‐ 0 Gifts
                ‐ 3 Cookies
                . . . . . .
                . . . . . .
                x x x x . .
                . . . x . .
                . . . Y . .
5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End
                You've collected:
                ‐ 0 Christmas decorations
                ‐ 0 Gifts
                ‐ 0 Cookies
                x .
                Y x
                x x
                x .
                x G
"""


def read_matrix():
    rows, cols = [int(x) for x in input().split(', ')]
    return [[x for x in input().split()] for _ in range(rows)]


def print_(mtrx):
    for r in mtrx:
        print(' '.join(str(x) for x in r))


def start_psn(mtrx):
    for idx, r in enumerate(mtrx):
        if 'Y' in r:
            c = r.index('Y')
            r = idx
            return r, c


def move(way, count):
    cur_row, cur_col = start_psn(maze)
    move_mapper = {
        'right': (0, 1),
        'left': (0, -1),
        'up': (-1, 0),
        'down': (1, 0),
    }
    for _ in range(count):
        next_row = move_mapper[way][0] + cur_row
        next_col = move_mapper[way][1] + cur_col
        next_row, next_col = move_validate(next_row, next_col)
        check_cell(next_row, next_col)
        maze[cur_row][cur_col] = 'x'
        maze[next_row][next_col] = 'Y'
        cur_row, cur_col = next_row, next_col
        if count_goods() == 0:
            break

def move_validate(r, c):
    if r not in range(len(maze)):
        r = len(maze) - abs(r)
    if c not in range(len(maze[0])):
        c = len(maze[0]) - abs(c)

    return r, c


def check_cell(r, c):
    if maze[r][c] in result:
        result[maze[r][c]] += 1


def count_goods():
    count = 0
    for r in maze:
        for c in r:
            if c != "." and c != 'Y' and c != 'x':
                count += 1
    return count


maze = read_matrix()
goodies_count = count_goods()
command = input()
result = {
    'D': 0,
    'G': 0,
    'C': 0,
}
full_name = {
    'D': 'Christmas decorations',
    'G': 'Gifts',
    'C': 'Cookies',
}
while command != 'End':
    direction, steps = command.split('-')
    move(direction, int(steps))
    if count_goods() == 0:
        break
    command = input()


if count_goods() == 0:
    print("Merry Christmas!")
print("You've collected:")
for key, value in result.items():
    print(f"- {value} {full_name[key]}")
print_(maze)
