"""
Write a program to flatten several lists of numbers, received in the following format:
§ String with numbers or empty strings separated by '|'.
§ Values are separated by spaces (' ', one or several)
§ Order the output list from the last to the first received, and their values from left to right as shown below.
Input               Output
1 2 3 |4 5 6 | 7 8
                    7 8 4 5 6 1 2 3
7 | 4 5|1 0| 2 5 |3
                    3 2 5 1 0 4 5 7
1| 4 5 6 7 | 8 9
                    8 9 4 5 6 7 1
"""


def unflatten_list():
    SIZE = 3
    ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mtrx = [[] for _ in range(SIZE)]
    for row in range(SIZE):
        for idx in range(row * 3, (row + 1) * SIZE):
            mtrx[row].append(ll[idx])

    comprehension = [[ll[idx] for idx in range(row * SIZE, ((row + 1) * SIZE))] for row in range(SIZE)]


def flatten_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return [num for sublist in matrix for num in sublist]


