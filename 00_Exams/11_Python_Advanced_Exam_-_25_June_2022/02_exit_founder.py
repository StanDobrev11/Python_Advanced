"""
First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in
which they are received determines the order in which they will take turns. The first player starts first.
Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
 Only one Exit ‐ marked with the "E" letter
 Trap (one, many, or none) ‐ marked with the "T" letter
 Wall (one, many, or none) ‐ marked with the "W" letter
 Empty positions will be marked with "."
In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving
coordinates for each of the players. They will be taking turns and stepping on different positions on the board until
one of them find the Exit or falls into a Trap. Here are the rules:
 If a player hits the letter "E", he escapes the maze and wins the game.
o Print "{player} found the Exit and wins the game!" and end the program.
 If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
o Print "{player} is out of the game! The winner is {winner}." and end the
program.
 If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
o Print "{player} hits a wall and needs to rest."
 If a player steps on an empty position ".", nothing happens.
 Both players can step in the same position at the same time.
Input
 On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
 On the following 6 lines, you will receive the maze board (elements will be separated by a space)
 On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
Output
 You should print the output as described above.
 The input coordinates will always be valid.

Input       Output              Comment
Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)
            Tom hits a wall and needs to rest.
            Jerry is out of the game! The winner is Tom.
                                First is Tom. He moves to
                                position (3, 2). He hits a wall
                                and needs to rest.
                                Next is Jerry. He moves to
                                position (1, 3). It is an empty
                                position.
                                Tom's next move (5, 1) is
                                ignored because he is resting.
                                Jerry moves to (5, 1). There is
                                a trap, so he is out of the
                                game. The program ends.
Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)
            Jerry found the Exit and wins the game!
Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)
            Jerry hits a wall and needs to rest.
            Tom hits a wall and needs to rest.
            Tom hits a wall and needs to rest.
            Jerry hits a wall and needs to rest.
            Tom found the Exit and wins the game!
"""
from collections import deque


def read_matrix():
    return [[x for x in input().split(' ')] for _ in range(6)]


def print_matrix():
    for r in matrix:
        print(' '.join(r))


def exit_game(player):
    print(f"{player} found the Exit and wins the game!")
    raise SystemExit


def fall_in_trap(player):
    print(f"{player} is out of the game! The winner is {players[1]}.")
    raise SystemExit


def hits_a_wall(player):
    print(f"{player} hits a wall and needs to rest.")
    to_rest.add(player)


def play(plrs, mtrx, rest):
    mapper = {
        'E': exit_game,
        'T': fall_in_trap,
        'W': hits_a_wall,
    }

    while True:

        row, col = eval(input())
        current_player = plrs[0]

        if current_player in rest:
            plrs.rotate()
            rest.remove(current_player)
            continue

        cell = mtrx[row][col]
        if cell in mapper:
            mapper[cell](current_player)

        plrs.rotate()


if __name__ == "__main__":
    players = deque(input().split(', '))
    matrix = read_matrix()
    to_rest = set()
    play(players, matrix, to_rest)
