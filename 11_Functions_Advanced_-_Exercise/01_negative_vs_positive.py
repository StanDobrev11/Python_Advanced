"""
You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from
the positive. Find the total sum of the negatives and positives, and print the following:
• On the first line, print the sum of the negatives
• On the second line, print the sum of the positives
• On the third line:
    o If the absolute negative number is larger than the positive number:
    "The negatives are stronger than the positives"
    o If the positive number is larger than the absolute negative number:
    "The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.
Input                               Output
1 2 -3 -4 65 -98 12 57 -84
                                    -189
                                    137
                                    The negatives are stronger than the positives
1 2 3
                                    0
                                    6
                                    The positives are stronger than the negatives
"""


def read_input():
    return [int(x) for x in input().split()]


def sum_positive(numbers, current_sum=0):
    for num in numbers:
        if num > 0:
            current_sum += num
    return current_sum


def sum_negative(numbers, current_sum=0):
    for num in numbers:
        if num < 0:
            current_sum += num
    return current_sum


nums = read_input()
positive_sum = sum_positive(nums)
negative_sum = sum_negative(nums)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
