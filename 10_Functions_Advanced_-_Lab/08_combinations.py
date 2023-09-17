"""
Write a program that receives names on the first line (separated by comma and space ", ") and number of chairs
on the second line (an integer). Find all the ways to fit those people on the chairs. Print each combination
on a separate line.
Note: In the example below, "Peter, George" is same as "George, Peter", so we only print the first combination
Input                   Output
Peter, George, Amy, Krasen
2
                        Peter George, Peter Amy, George Amy
"""
from collections import deque


def read_input():
    return input().split(', ')


def recursive_combinations(data, comb_size, result):
    if len(result) == comb_size:
        print(result)
        return
    for idx in range(len(data)):
        name = data[idx]
        result.append(name)
        recursive_combinations(data[idx + 1:], comb_size, result)
        result.pop()


def print_result(result):
    pass


data = read_input()
combination_size = int(input())

recursive_combinations(data, combination_size, [])
