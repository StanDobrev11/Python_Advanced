"""
Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
Submit only the function in the judge system.


Test Code                                       Output
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
                                                [2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
                                                [1, 3, 5, 7, 9]

"""


def even_odd(*args):
    def even():
        return [x for x in args[:-1] if int(x) % 2 == 0]

    def odd():
        return [x for x in args[:-1] if int(x) % 2 == 1]

    command = args[-1]
    if command == 'even':
        return even()
    else:
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
