"""
Write function called best_list_pureness which will receive a list of numbers and a number K. You have to
rotate the list K times (last becomes first) to find the variation of the list with the best pureness (pureness is
calculated by summing all the elements in the list multiplied by their indices). For example, in the list [4, 3, 2,
6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At the end the function should return a string
containing the highest pureness and the amount of rotations that were made to find this pureness in the following
format: "Best pureness {pureness_value} after {count_rotations} rotations". If there is more
than one highest pureness, take the first one.
Note: Submit only the function in the judge system
Input
 There will be no input, just parameters passed to your function
Output
 There is no expected output
 The function should return a string in the following format: "Best pureness {pureness_value}
after {count_rotations} rotations"

Test Code                   Output                  Comment
test = ([4, 3, 2, 6], 4)
result =
best_list_pureness(*test)
print(result)
                            Best pureness 26 after 3
                            rotations
                                                    Rotation 0 ‐> Pureness 25
                                                    Rotation 1 ‐> Pureness 16
                                                    Rotation 2 ‐> Pureness 23
                                                    Rotation 3 ‐> Pureness 26
                                                    Rotation 4 ‐> Pureness 25
test = ([7, 9, 2, 5, 3,
4], 3)
result =
best_list_pureness(*test)
print(result)
                            Best pureness 78 after 2
                            rotations
                                                    Rotation 0 ‐> Pureness 60
                                                    Rotation 1 ‐> Pureness 66
                                                    Rotation 2 ‐> Pureness 78
                                                    Rotation 3 ‐> Pureness 78
test = ([1, 2, 3, 4, 5],
10)
result =
best_list_pureness(*test)
print(result)
                            Best pureness 40 after 0
                            rotations
"""
from collections import deque


def best_list_pureness(*args):
    el_queue = deque(args[0])
    rotations = args[1]
    result = {}
    for rotation in range(rotations + 1):
        max_value = 0
        for idx, el in enumerate(el_queue):
            max_value += el * idx
        result[rotation] = max_value
        el_queue.rotate()
    result = sorted(result.items(), key=lambda x: -x[1])[0]

    return f'Best pureness {result[1]} after {result[0]} rotations'


test = ([1, 2, 3, 4, 5],
10)
result = best_list_pureness(*test)
print(result)
