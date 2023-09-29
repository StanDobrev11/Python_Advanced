"""
You will be given a matrix with 7 rows and 7 columns representing the dartboard.
Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.
The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or
less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate information of a hit will
be in the format: "({row}, {column})".
 If a player hits outside the dartboard, he does not score any points.
 If a player hits a number, it is deducted from his total.
 If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then
deducted from his total.
 If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then
deducted from his total.
 "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are
deducted from his total.
Your job is to find who won the game and with how many turns.
Input
 The name of the first player and the name of the second player, separated by ", "
 7 lines – the dartboard (separated by single space)
 On the next lines ‐ the coordinates in the format: "({row}, {column})"
Output
 You should print only one line containing the winner and his count of throws:
"{name} won the game with {count_turns} throws!"
Constrains
 There will always be exactly 7 lines
 There will always be a winner
 The points will be in range [1, 24]
 The coordinates will be in range [0, 100]
Input               Output
Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)
                    Ivan won the game with 1
                    throws!
George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
                    Hristo won the game with
                    4 throws!
"""
from collections import deque
from math import ceil


def read_matrix():
    return [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(7)]


def check_result():
    if any(value <= 0 for value in players.values()):
        return True
    return False


players = {x: 501 for x in input().split(', ')}
dashboard = read_matrix()

turn = deque([name for name in players.keys()])
shots_made = 1
while True:

    current_player = turn[0]
    row, col = eval(input())

    if row not in range(7) or col not in range(7):
        # If a player hits outside the dartboard, he does not score any points.
        turn.rotate()
        shots_made += 1
        continue

    hit = dashboard[row][col]

    if isinstance(hit, int):  # If a player hits a number, it is deducted from his total.
        players[current_player] -= hit

    if hit == 'D':
        # If a player hits a "D" the sum of the 4 corresponding numbers per column and row is
        # doubled and then deducted from his total.
        points = 2 * (dashboard[row][0] + dashboard[row][6] + dashboard[0][col] + dashboard[6][col])
        players[current_player] -= points

    if hit == 'T':
        # If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and
        # then deducted from his total.
        points = 3 * (dashboard[row][0] + dashboard[row][6] + dashboard[0][col] + dashboard[6][col])
        players[current_player] -= points

    if hit == 'B' or check_result():
        print(f"{turn[0]} won the game with {ceil(shots_made / 2)} throws!")
        raise SystemExit

    turn.rotate()
    shots_made += 1
