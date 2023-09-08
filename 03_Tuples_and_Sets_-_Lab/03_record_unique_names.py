"""
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matt

Input      Output
8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
            Alan
            Joey
            Lee
            Joe
            Peter
"""


def read_input_to_list(count):
    input_list = []
    for _ in range(count):
        input_list.append(input())
    return input_list


def print_result(result):
    for el in result:
        print(el)


n = int(input())

names = read_input_to_list(n)
names = set(names)

print_result(names)
