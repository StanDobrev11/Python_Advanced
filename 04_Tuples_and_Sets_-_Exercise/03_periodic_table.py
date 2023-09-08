"""
Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n - the
count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds
separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter):

Input       Output
4
Ce O
Mo O Ce
Ee
Mo
            Ce
            Ee
            Mo
            O
3
Ge Ch O Ne
Nb Mo Tc
O Ne
            Ch
            Ge
            Mo
            Nb
            Ne
            O
            Tc
"""


def add_fm_input(items_count: int) -> set:
    current_set = set()
    for _ in range(items_count):
        item = input().split()
        for el in item:
            current_set.add(el)
    return current_set


def print_result(result):
    for el in result:
        print(el)


number_of_lines = int(input())
unique_lines = add_fm_input(number_of_lines)
print_result(unique_lines)
