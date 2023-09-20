"""
Write a function called list_manipulator which receives a list of numbers as first parameter and different
amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be
"beginning" or "end". There might or might not be any other parameters (numbers):
 In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers
and return the new list
 In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the
new list
 In case of "remove" and "beginning"
o If there is another parameter (number), remove that amount of numbers from the beginning of the
list of numbers.
o If there are no other parameters, remove only the first element of the list.
o Finaly, return the new list
 In case of "remove" and "end"
o If there is another parameter (number), remove that amount of numbers from the end of the list of
numbers.
o Otherwise if there are no other parameters, remove only the last element of the list.
o Finaly, return the new list
For more clarifications, see the examples below.
Input
 There will be no input
 Parameters will be passed to your function
Output
 The function should return the new list of numbers

print(list_manipulator([1,2,3], "remove", "end"))
                                                                [1, 2]
print(list_manipulator([1,2,3], "remove", "beginning"))
                                                                [2, 3]
print(list_manipulator([1,2,3], "add", "beginning", 20))
                                                                [20, 1, 2, 3]
print(list_manipulator([1,2,3], "add", "end", 30))
                                                                [1, 2, 3, 30]
print(list_manipulator([1,2,3], "remove", "end", 2))
                                                                [1]
print(list_manipulator([1,2,3], "remove", "beginning", 2))
                                                                [3]
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
                                                                [20, 30, 40, 1, 2, 3]
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
                                                                [1, 2, 3, 30, 40, 50]
"""


def list_manipulator(nums, *args):
    command, position = args[0], args[1]

    if command == 'add':
        if position == 'beginning':
            return list(args[2:]) + nums
        else:
            return nums + list(args[2:])

    elif command == 'remove':
        try:
            count = args[2]
        except IndexError:
            count = 1

        if position == 'beginning':
            for _ in range(count):
                nums.pop(0)
        else:
            for _ in range(count):
                nums.pop()

        return nums


print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
