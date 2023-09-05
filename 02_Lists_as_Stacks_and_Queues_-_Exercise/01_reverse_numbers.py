"""
Write a program that reads a string with N integers from the console, separated by a single space, and reverses
them using a stack. Print the reversed integers on one line, separated by a single space.

Input       Output
1 2 3 4 5   5 4 3 2 1
1            1
"""
lst_int = input().split()

for _ in range(len(lst_int)):
    print(lst_int.pop(), end=' ')
