"""
You will be given an integer n for the size of the mines field with square shape and another one for the number of
bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb. Your task
is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate the
numbers in each cell of the field. Each cell represents a number of all bombs directly near it (up, down, left, right and
the 4 diagonals).

Input
 On the first line, you are given the integer n – the size of the square matrix.
 On the second line – the number of the bombs.
 The next n lines holds the position of each bomb.
Output
 Print the matrix you've created.
Constraints
 The size of the square matrix will be between [2…15].

Input   Output
4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)
        1 1 2 *
        1 * 3 2
        2 3 * 1
        * 2 1 1
5
3
(1, 1)
(2, 4)
(4, 1)
        1 1 1 0 0
        1 * 1 1 1
        1 1 1 1 *
        1 1 1 1 1
        1 * 1 0 0
"""


def print_(field):
    for row in field:
        print(' '.join(str(x) for x in row))


def create_mine_field():
    size = int(input())
    return [[0] * size for _ in range(size)]


def place_mines(field):
    mines = int(input())
    mine_list = []
    for _ in range(mines):
        mine = tuple(int(x) for x in input() if x.isdigit())
        r, c = mine
        if is_valid(r) and is_valid(c):
            mine_list.append(mine)
            if field[r][c] == '*':
                mine_list.remove(mine)
            field[r][c] = '*'
    return field, mine_list


def is_valid(x):
    if x in range(len(mine_field)):
        return True
    return False


def cells_surrounding_mine(field, coordinates):
    for mine in coordinates:
        mine_r, mine_c = mine
        for r in range(mine_r - 1, mine_r + 2):
            if is_valid(r):
                for c in range(mine_c - 1, mine_c + 2):
                    if is_valid(c):
                        if isinstance(field[r][c], int):
                            field[r][c] += 1
    return field


mine_field = create_mine_field()
mine_field, mines_coordinates = place_mines(mine_field)
mine_field = cells_surrounding_mine(mine_field, mines_coordinates)
print_(mine_field)
