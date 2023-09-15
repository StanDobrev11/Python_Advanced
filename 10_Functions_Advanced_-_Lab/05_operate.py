"""
Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple
numbers (integers) as additional arguments (*args). The function should return the result of the operator
applied to all the numbers. For more clarification, see the examples below.
Submit only your function in the Judge system.

Note: Be careful when you have multiplication and division
Test Code               Output                  Comment
print(operate("+", 1, 2, 3))
                        6
                                                1 + 2 + 3 = 6
print(operate("*", 3, 4))
                        12
                                                3 * 4 = 12
"""
from functools import reduce


# def operate(operator, *args):
#     return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


# def operate(operator, *args):
#     if operator == '+':
#         return reduce(lambda x, y: x + y, args)
#     if operator == '-':
#         return reduce(lambda x, y: x - y, args)
#     if operator == '*':
#         return reduce(lambda x, y: x * y, args)
#     if operator == '/':
#         return reduce(lambda x, y: x / y, args)


def operate(operator, *args):
    return reduce(mapper[operator], args)


mapper = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 20, 5))
print(operate("-", 3, 4))
