"""
Write a program that prints a set of elements.
On the first line, you will receive two numbers - n and m, separated by a single space - representing the lengths of
two separate sets. On the next n + m lines, you will receive n numbers,
which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that
appear in both and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}

Input Output
4 3
1
3
5
7
3
4
5
        3
        5
2 2
1
3
1
5
        1
"""


def add_fm_input(items_count: int) -> set:
    current_set = set()
    for _ in range(items_count):
        item = int(input())
        current_set.add(item)
    return current_set


def print_result(result):
    for el in result:
        print(el)


first_num_of_items, second_num_of_items = [int(x) for x in input().split()]

first_set = add_fm_input(first_num_of_items)
second_set = add_fm_input(second_num_of_items)
common_elements_set = first_set.intersection(second_set)
print_result(common_elements_set)
