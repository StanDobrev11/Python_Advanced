"""
A hungry little mouse is living in an old suburbs house. It walks around the kitchen cupboard every night and eats all
the cheese. A lazy plump cat is guarding the kitchen, so the mouse should not walk out of the cupboard area.
In the beginning, you will be given N and M – integers, separated by a comma ‐ ",", indicating the cupboard’s area
dimensions. On the next N lines, you will receive strings, representing the rows of the area, with M columns.
After that, on each line, until the command "danger" appears as an input string, you will receive the possible
directions for the mouse to move ‐ "up", "down", "right", and "left".
If the mouse steps outside the cupboard area, the cat will attack, and the cheese hunt is over. In that case, the
program ends, keep the last known position of the mouse, before it steps outside the cupboard area and the
following message is printed on the Console: "No more cheese for tonight!"
Possible characters in the matrix are:
 M ‐ represents the mouse's position.
 C – represents a piece of cheese.
 * – represents an empty position, nothing happens if the mouse steps on it.
 @ – represents a wall in the cupboard, cannot step on or go through it.
 T – represents a trap.
The mouse starts from the M ‐ position.
 If the mouse steps on C – position, it eats the cheese from the field, and the position is marked with "*".
o If this is the last cheese in the cupboard area, the mouse goes to sleep. Remember that this will be
the last known position of the mouse. The program ends and the following message is printed on
the Console: "Happy mouse! All the cheese is eaten, good night!"
 If the mouse steps into a trap (T ‐position), it will be trapped. Remember that this will be the last known
position of the mouse. In that case, the program ends, and the following message is printed on the Console:
"Mouse is trapped!"
 If the given direction leads the mouse towards @ ‐ position, this is a wall in the cupboard area. Do not
make the move and skip the command.
 If the "danger" command is received before the mouse manages to eat all the cheese, the mouse
disappears. Remember that this will be the last known position of the mouse and you will need it for the
final state of the matrix. In that case, the program ends, and the following message is printed on the
Console: "Mouse will come back later!"
In the end, print the final state of the matrix (cupboard area) with the last known position of the mouse in it. Each
row on a new line.
Input
 On the first line you will get the number of rows and columns of the matrix, separated by a comma.
 On the next N lines, you will receive strings, representing each row of the matrix.
 On each of the following lines, until the command "danger" appears as an input string, you will receive the
possible directions for the mouse to move ‐ "up", "down", "right", and "left".
 "danger" command – The mouse spots danger and disappears… for now!
Output
 On the first line:
o If the mouse steps outside the cupboard
"No more cheese for tonight!"
o If the mouse manages to eat all the cheese
"Happy mouse! All the cheese is eaten, good night!"
o If the mouse steps into a trap (T ‐position)
"Mouse is trapped!"
o If the "danger" command is received before the mouse manages to eat all the cheese –
"Mouse will come back later!"
 On the next lines, print the final state of the matrix with the last known position of the mouse in it. Each
row ‐ on a new line, each row position with NO separator.
Constraints
 There will always be at least one trap in the cupboard.
 There will always be some cheese in the cupboard.
 There will always be а "danger" command in the end, but it is not necessary to reach it. The program may
end earlier.
 Each row of the matrix will have the same length.
Input       Output
5,5
**M**
T@@**
CC@**
**@@*
**CC*
left
down
left
down
down
down
right
danger
            Mouse is trapped!
            *****
            M@@**
            CC@**
            **@@*
            **CC*
4,8
CC@**C*M
T*@**CT*
**@@@@**
T***C***
down
right
left
down
left
danger
            No more cheese for tonight!
            CC@**C**
            T*@**CTM
            **@@@@**
            T***C***
6,3
@CC
@TC
@C*
@M*
@**
@**
left
up
left
right
up
up
left
left
danger
            Happy mouse! All the cheese
            is eaten, good night!
            @M*
            @T*
            @**
            @**
            @**
            @**
"""


def read_area(n):
    return [[x for x in list(input())] for _ in range(n)]


def print_area():
    for row in area:
        print(''.join(row))


def mouse_position():
    for idx, row in enumerate(area):
        if 'M' in row:
            col = row.index('M')
            row = idx
            return row, col


def valid_position(row, col):
    if row not in range(rows) or col not in range(cols):
        return False
    return True


def all_cheese_count():
    cheese_count = 0
    for row in range(rows):
        for col in range(cols):
            if area[row][col] == 'C':
                cheese_count += 1

    return cheese_count


def explore_area():
    global cheese
    direction = input()
    row, col = mouse_position()
    while direction != 'danger':
        drow, dcol = direction_mapper[direction]
        next_row, next_col = row + drow, col + dcol

        if valid_position(next_row, next_col):
            cell = area[next_row][next_col]
            if cell == '*':
                area[row][col] = '*'
                area[next_row][next_col] = 'M'
            elif cell == 'C':
                cheese -= 1
                area[row][col] = '*'
                area[next_row][next_col] = 'M'
                if cheese <= 0:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    print_area()
                    raise SystemExit
            elif cell == 'T':
                area[row][col] = '*'
                area[next_row][next_col] = 'M'
                print("Mouse is trapped!")
                print_area()
                raise SystemExit
            else:
                direction = input()
                continue

        else:
            print("No more cheese for tonight!")
            print_area()
            raise SystemExit

        row, col = next_row, next_col
        direction = input()

    print("Mouse will come back later!")
    print_area()


if __name__ == "__main__":
    direction_mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    rows, cols = [int(x) for x in input().split(',')]
    area = read_area(rows)
    cheese = all_cheese_count()
    explore_area()
