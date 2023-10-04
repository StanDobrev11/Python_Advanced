"""
Blind man's buff is played in a spacious area, such as outdoors or in a large room, in which one player, is blindfolded
and gropes around attempting to touch the other players without being able to see them…
You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive
the rows of the playground, with M columns. You will be marked with the letter 'B', and placed in a random
position. In random positions, furniture or other obstacles will be marked with the letter 'O'. The other players
(opponents) will be marked with the letter 'P'. There will always be three other players participating in the game.
All of the empty positions will be marked with '‐'.
Your goal is to touch as many players as possible during the game, without leaving the playground or stepping on an
obstacle.
On the next few lines, until you receive the command "Finish", you will receive a few lines with commands
representing which direction you need to move. The possible directions are "up", " down", "right", and "left". If
the direction leads you out of the field, you need to stay in position inside the field(do NOT make the move). If you
have an obstacle, towards the direction, do NOT make the move and wait for the next command.
You need to keep track of the count of touched opponents and the moves you’ve made.
In case you step on a position marked with '‐', increase the count of the moves made.
When you receive a command with direction, you check the position you need to step on for an obstacle or
opponent. If there is an opponent, you touch him and the position is marked with '‐'(increase the count of the
touched opponents and moves made), and this is your new position.
The game is over when you manage to touch all other opponents or the given command is "Finish". A game report
is printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
Input
 On the first line, you'll receive the dimensions of the playground in the format: "N M", where N is the number
of rows, and M is the number of columns. They'll be separated by a single space (" ").
 On the next N lines, you will receive a string representing the respective row of the playground. The positions
in every string will be separated by a single space (" ").
 On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right,
left).
Output
 When the game is over, the following output should be printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
Constraints
 The playground size will be a 32‐bit integer in the range [2 … 2 147 483 647].
 The playground will always have three opponents in it ‐ 'P'.
 The obstacles on the playground will always be random count, and there will be cases without any obstacles.
Input           Output
5 8
- - - O - P - O
- P - O O - - -
- - - - - - O -
- P B - O - - O
- - - O - - - -
left
left
left


up
up
left
Finish
                Game over!
                Touched opponents: 1 Moves made: 3
4 4
O B O -
- P O P
- - P -
- - - -
left
right
down
right
down
right
up
right
up
down
Finish
            Game over!
            Touched opponents: 3 Moves made: 5
"""


def read_playground(n):
    return [[x for x in input().split()] for _ in range(n)]


def print_playground():
    for row in playground:
        print(' '.join(row))


def seeker_position():
    for idx, row in enumerate(playground):
        if 'B' in row:
            col = row.index('B')
            row = idx
            return row, col


def valid_position(row, col):
    if row not in range(playground_rows) or col not in range(playground_cols):
        return False
    return True


def move_to_position(course, row, col):
    next_row = row + direction_mapper[course][0]
    next_col = col + direction_mapper[course][1]

    if valid_position(next_row, next_col):
        location = playground[next_row][next_col]
    else:
        return row, col

    try:
        playground_mapper[location]()
    except KeyError:
        return row, col

    playground[row][col] = '-'
    playground[next_row][next_col] = 'B'
    return next_row, next_col


def begin_battle():
    row, col = seeker_position()
    direction = input()
    while direction != 'Finish':
        row, col = move_to_position(direction, row, col)

        if opponent_caught == 3:
            break
        direction = input()

    return print_outcome()


def catch_opponent():
    global opponent_caught, moves_made
    opponent_caught += 1
    moves_made += 1


def free_step():
    global moves_made
    moves_made += 1


def print_outcome():
    print("Game over!")
    print(f"Touched opponents: {opponent_caught} Moves made: {moves_made}")


if __name__ == "__main__":
    direction_mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }
    playground_mapper = {
        'P': catch_opponent,
        '-': free_step,
    }
    moves_made = 0
    opponent_caught = 0
    playground_rows, playground_cols = [int(x) for x in input().split()]
    playground = read_playground(playground_rows)
    begin_battle()
