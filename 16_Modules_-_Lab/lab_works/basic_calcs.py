from functools import reduce


def sum_num(a, b):
    return a + b


def subtract_num(a, b):
    return a - b


def multiply_num(a, b):
    return a * b


def divide_num(a, b):
    return a / b


def pow_num(a, b):
    return a ** b


mapper = {
    '+': sum_num,
    '-': subtract_num,
    '*': multiply_num,
    '/': divide_num,
    '^': pow_num,
}


def calculate_string(string):
    a, operator, b = string.split()
    a, b = float(a), float(b)
    return f"{mapper[operator](a, b):.2f}"

