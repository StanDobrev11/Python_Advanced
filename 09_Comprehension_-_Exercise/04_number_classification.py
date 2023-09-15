"""
Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
and prints all the positive, negative, even and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
Input               Output
1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
                    Positive: 1, 0, 5, 3, 4, 12, 19
                    Negative: -2, -100, -20, -33
                    Even: -2, 0, 4, -100, -20, 12
                    Odd: 1, 5, 3, 19, -33
"""


def read_input():
    return input().split(', ')


def cast_to_int():
    return [int(x) for x in read_input()]


def positive(nums):
    return [x for x in nums if x >= 0]


def negative(nums):
    return [x for x in nums if x < 0]


def even(nums):
    return [x for x in nums if x % 2 == 0]


def odd(nums):
    return [x for x in nums if x >= 1]


nums = cast_to_int()
dd = {
    'Positive': positive(nums),
    'Negative': negative(nums),
    'Even': even(nums),
    'Odd': odd(nums),
}

for item, value in dd.items():
    print(f'{item}: {", ".join(map(str, value))}')
