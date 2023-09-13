"""
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size of the field. In the following few lines, you will be
given a field with:
• One bunny - randomly placed in it and marked with the symbol "B"
• Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The
directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of
the directions, you should not consider the fields after the trap in this direction. The bunny can move within the field
and cannot go outside its boundaries. Do not consider negative indices as valid ones. For more clarifications, see the
examples below.
Note: In some directions, the collected eggs can happen to be zero or a negative number.
Input
• A number representing the size of the field
• The matrix representing the field (each position separated by a single space)
Output
• The direction which should be considered as best (lowercase)
• The field positions from which we are collecting eggs as lists
• The total number of eggs collected
Constraints
• There will NOT be two or more paths consisting of the same total amount of eggs
Input       Output      Comment
5
1 3 7 9 11
X 5 4 X 63
-170 3 21 95 1
B -100 0 0 -100
-100 2 33 2 0
            right
            [3, 1]
            [3, 2]
            [3, 3]
            [3, 4]
            87
                        The number of eggs if the bunny goes up is equal to 7. If it goes
                        down = 9, there are no eggs on the left and 87 on the right. That's
                        why the bunny should follow this direction (right) and collect the
                        eggs provided there.
8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22

            down
            [6, 2]
            [7, 2]
            113
"""


def read_matrix():
    rows = int(input())
    return [[x if x.isalpha() else int(x) for x in input().split()] for _ in range(rows)]


def find_start_psn(mtrx):
    for idx, r in enumerate(mtrx):
        if 'B' in r:
            c = r.index('B')
            r = idx
            return r, c


def find_best_sum(direction, mtrx, r, c, max_sum, coor_list, value_to_coor):
    if r not in range(len(mtrx)) or c not in range(len(mtrx)) or mtrx[r][c] == 'X':
        coor_list.append(max_sum)
        value_to_coor[direction] = coor_list
        return value_to_coor
    max_sum += mtrx[r][c]
    coor_list.append([r, c])
    if direction == 'right':
        c += 1
    elif direction == 'left':
        c -= 1
    elif direction == 'up':
        r -= 1
    elif direction == 'down':
        r += 1
    return find_best_sum(direction, mtrx, r, c, max_sum, coor_list, value_to_coor)


def print_result(result):
    key = find_max(result)
    value = result[key].pop()
    print(key)
    for coordinates in result[key]:
        print(coordinates)
    print(value)


def find_max(result):
    max_value = -float('inf')
    max_key = ''
    for key, values in result.items():
        if len(values) == 1:
            continue
        value = values[-1]
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


matrix = read_matrix()
row, col = find_start_psn(matrix)

value_to_coordinates = {}
right = find_best_sum('right', matrix, row, col + 1, 0, [], value_to_coordinates)
left = find_best_sum('left', matrix, row, col - 1, 0, [], value_to_coordinates)
up = find_best_sum('up', matrix, row - 1, col, 0, [], value_to_coordinates)
down = find_best_sum('down', matrix, row + 1, col, 0, [], value_to_coordinates)
print_result(value_to_coordinates)
