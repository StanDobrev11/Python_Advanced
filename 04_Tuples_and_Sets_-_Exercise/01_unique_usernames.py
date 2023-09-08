"""
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique
ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the
collection on the console (the order does not matter):

Input           Output
6
George
George
George
Peter
George
NiceGuy1234
                George
                Peter
                NiceGuy1234
10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George
                Peter
                Maria
                George
                Steve
                Alex
"""


def read_input_to_list(count):
    input_set = set()
    for _ in range(count):
        input_set.add(input())
    return input_set


def print_result(result):
    for el in result:
        print(el)


count_of_users = int(input())
usernames = read_input_to_list(count_of_users)
print_result(usernames)
