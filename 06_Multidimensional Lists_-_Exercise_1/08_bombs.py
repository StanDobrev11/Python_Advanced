"""
You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a
new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single space,
in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb
explodes, it deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals).
One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or
below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the
dead ones).
Input
• On the first line, you are given the integer N - the size of the square matrix.
• The following N lines hold each column's values - N numbers separated by a space.
• On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
• On the first line, you need to print the count of all alive cells in the format:
"Alive cells: {alive_cells}"
• On the second line, you need to print the sum of all alive cells in the format:
"Sum: {sum_of_cells}"
• In the end, print the matrix. A space must separate the cells.
Constraints
• The size of the matrix will be between [0…1000].
• The bomb coordinates will always be in the matrix.
• The bomb's values will always be greater than 0.
• The integers of the matrix will be in the range [1…10000].
Input           Output          Comments
4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
                Alive cells: 3
                Sum: 12
                8 -4 -5 -2
                -3 -3 0 2
                0 0 -4 -1
                -3 -1 -1 2
                                1) The bomb with value 7 will explode and reduce the values of the cells
                                around it.
                                2) The bomb with coordinates 2,1 and value 9 will explode and reduce its
                                neighbor cells.
                                3) The bomb with coordinates 2,0 and value 9 will explode.
                                After that, you have to print the count of the alive cells - 3, and their sum
                                - 12. Print the matrix after the explosions.
3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2
                Alive cells: 3
                Sum: 8
                4 1 0
                0 -3 -8
                3 -8 0

5
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
"""
from collections import deque


def read_matrix():
    dims = int(input())
    return [[int(x) for x in input().split(' ')] for _ in range(dims)], dims


def read_bombs():
    bombs = []
    bomb_line = [x for x in input().split(' ')]
    for bomb in bomb_line:
        row, col = [int(x) for x in bomb.split(',')]
        bombs.append((row, col))
    return bombs


def is_middle_cell(mtrx, row, col):
    if row in range(1, len(mtrx) - 1) and col in range(1, len(mtrx) - 1):
        return True


def is_border_cell(mtrx, row, col):
    if row not in range(1, len(mtrx) - 1) and col in range(1, len(mtrx) - 1):
        return True
    if row in range(1, len(mtrx) - 1) and col not in range(1, len(mtrx) - 1):
        return True


def detonate(bombs, mtrx):
    power, coordinates = get_bomb_power_coordinates(bombs, mtrx)
    if power <= 0:
        return
    row, col = coordinates
    if is_middle_cell(mtrx, row, col):
        detonate_middle(mtrx, power, coordinates)

    elif is_border_cell(mtrx, row, col):
        detonate_border(mtrx, power, coordinates)
    else:
        detonate_corner(mtrx, power, coordinates)


def detonate_middle(mtrx, power, coordinates):
    top_left = coordinates
    row, col = top_left[0] - 1, top_left[1] - 1
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if mtrx[r][c] > 0:
                mtrx[r][c] -= power


def detonate_border(mtrx, power, coordinates):
    row, col = coordinates
    rows = 2
    cols = 2
    if row == 0:
        row, col = (row, col - 1)
        cols += 1
    elif row == len(mtrx) - 1:
        row, col = (row - 1, col - 1)
        cols += 1
    elif col == 0:
        row, col = (row - 1, col)
        rows += 1
    elif col == len(mtrx) - 1:
        row, col = (row - 1, col)
        rows += 1
    for r in range(row, row + rows):
        for c in range(col, col + cols):
            if mtrx[r][c] > 0:
                mtrx[r][c] -= power


def detonate_corner(mtrx, power, coordinates):
    row, col = coordinates
    if row == len(mtrx) - 1 and col == len(mtrx[0]) - 1:
        row -= 1
        col -= 1
    elif row == len(mtrx) - 1:
        row -= 1
    elif col == len(mtrx[0]) - 1:
        col -= 1
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            if mtrx[r][c] > 0:
                mtrx[r][c] -= power


def get_bomb_power_coordinates(bombs, mtrx):
    next_bomb = bombs.popleft()
    row, col = next_bomb
    power = mtrx[row][col]
    return power, (row, col)


def get_matrix_sum(mtrx):
    the_sum = 0
    count = 0
    for row in mtrx:
        for col in row:
            if col > 0:
                the_sum += col
                count += 1
    return the_sum, count


def print_matrix(mtrx, value, count):
    print(f'Alive cells: {count}')
    print(f'Sum: {value}')
    for row in mtrx:
        print(f'{" ".join(map(str, row))}')


matrix, size = read_matrix()

bombs_list = read_bombs()
# while not bombs_list == 'End':
bombs = deque(bombs_list)
for _ in range(len(bombs_list)):
    detonate(bombs, matrix)

matrix_value, count = get_matrix_sum(matrix)
print_matrix(matrix, matrix_value, count)

# bombs_list = read_bombs()
