"""
The presents are ready, and Santa has to deliver them to the kids.
You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the cell
has an "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked with "V".
There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you
receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty
kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes
happy and extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if
naughty or nice). If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to
these cells, or if he does, he returns to the cell where the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
Keep in mind that you should check whether all the nice kids received presents.
Input
• On the first line, you are given the integer m - the count of presents
• On the second - integer n - the size of the neighborhood
• The following n lines hold the values for every row
• On each of the following lines you will get a command
Output
• On the first line:
o If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of
presents!"
• Next, print the matrix.
• In the end, print one of these messages:
o If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
o Otherwise, print:
"No presents for {count nice kids} nice kid/s."
Constraints
• The size of the square matrix will be between [2…10].
• Santa's position will be marked with an 'S'.
• There will always be at least 1 nice kid.
• There won't be a case where the cookie is on the border of the matrix
Input               Output                  Comments
5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
                    - - - -
                    - - - S
                    - - - -
                    X - - -
                    Good job, Santa! 2 happy nice kid/s.
                                            Santa has 5 presents. The size of the
                                            matrix is 4. After we receive the matrix,
                                            we start reading commands. The first one
                                            is "up". The "X" means there is a naughty
                                            kid, so Santa moves on without dropping
                                            any presents. Next, he reaches a nice kid
                                            and drops a present. The "down"
                                            command moves Santa to an empty cell.
                                            The last command before the "Christmas
                                            morning" message is "right". Again we
                                            have a nice kid. The count of nice kids
                                            reached 2, and we don't have any nice
                                            kids without presents left. So we print the
                                            appropriate message.
0
4
- - - -
V - X -
- X C -
- - - S
left
up
                    Santa ran out of presents!
                    - - - -
                    V - - -
                    - - S -
                    - - - -
                    No presents for 1 nice kid/s.
                                            The commands send Santa to a cell with
                                            a cookie, so all of the kids around him
                                            receive presents. He runs out of presents
                                            because we have 3 kids there and only 3
                                            presents. The program ends, and we
                                            have 1 nice kid that hasn't received a
                                            present.
"""


def read_matrix():
    rows = int(input())
    return [[x for x in input().split()] for _ in range(rows)]


def print_matrix(mtrx):
    for r in mtrx:
        print(' '.join(str(x) for x in r))


def find_start_psn(mtrx):
    for idx, r in enumerate(mtrx):
        if 'S' in r:
            c = r.index('S')
            r = idx
            return r, c


def get_nice_kids(mtrx):
    nice_kids = 0
    for r in mtrx:
        nice_kids += r.count('V')
    return nice_kids


def in_boundary(mtrx, r, c):
    if r not in range(len(mtrx)) or c not in range(len(mtrx)):
        return False
    return True


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


def move(mtrx, direction, cur_r, cur_c, presents):
    r, c = get_next_position(direction, cur_r, cur_c)
    if in_boundary(mtrx, r, c):
        mtrx[cur_r][cur_c] = '-'
        (r, c), presents = take_a_step(mtrx, r, c, presents)
        cur_r, cur_c = r, c
        mtrx[cur_r][cur_c] = 'S'
    return (cur_r, cur_c), presents


def take_a_step(mtrx, r, c, presents):
    cur_r, cur_c = r, c
    if mtrx[cur_r][cur_c] == 'V':
        presents -= 1
    elif mtrx[cur_r][cur_c] == 'C':
        presents = eat_cookies(mtrx, cur_r, cur_c, presents)

    return (r, c), presents


def eat_cookies(mtrx, cur_r, cur_c, presents):
    houses_to_check = {
        (cur_r, cur_c - 1),
        (cur_r, cur_c + 1),
        (cur_r - 1, cur_c),
        (cur_r + 1, cur_c),
    }
    for house in houses_to_check:
        r, c = house
        if in_boundary(mtrx, r, c):
            if mtrx[r][c] == 'V' or mtrx[r][c] == 'X':
                presents -= 1
                mtrx[r][c] = '-'
            if presents <= 0:
                return presents
    return presents


def print_result():
    nice_kids_left = get_nice_kids(matrix)
    if nice_kids_left > 0:
        if presents_count <= 0:
            print("Santa ran out of presents!")
            print_matrix(matrix)
            print(f"No presents for {nice_kids_left} nice kid/s.")
        else:
            print_matrix(matrix)
            print(f"No presents for {nice_kids_left} nice kid/s.")
    else:
        print_matrix(matrix)
        print(f"Good job, Santa! {nice_kids} happy nice kid/s.")


presents_count = int(input())
matrix = read_matrix()
row, col = find_start_psn(matrix)
nice_kids = get_nice_kids(matrix)
command = input()
while command != "Christmas morning":
    (row, col), presents_count = move(matrix, command, row, col, presents_count)
    if presents_count <= 0:
        break
    command = input()
print_result()
