"""
Write a function called numbers_searching which receives a different amount of parameters. All parameters will
be integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount of
duplicates from the given sequence and a missing value, such that all the duplicate values and the missing value
are between the smallest and the biggest received number.
The function should return a list with the last missing number as a first argument and a sorted list, containing the
duplicates found, in ascending order.
For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate
numbers in the following format: [3, [2, 4]]
Input
 There will be no input
 Parameters will be passed to your function
Output
 The function should return a list in the following format: [missing number, [duplicate_numbers separated
with comma and space]]
Constraints
 The missing number will always be between the smallest and the biggest received number

print(numbers_searching(1, 2, 4, 2, 5, 4))
                                                [3, [2, 4]]
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
                                                [6, [5, 7, 9]]
print(numbers_searching(50, 50, 47, 47, 48, 45, 49,
44, 47, 45, 44, 44, 48, 44, 48))
                                                [46, [44, 45, 47, 48, 50]]
"""


def numbers_searching(*args):
    nums = sorted(list(args))
    missing_nums = []
    for num in range(nums[0], nums[-1]):
        if num not in nums:
            missing_nums.append(num)
    nums = sorted(list(set(x for x in nums if nums.count(x) > 1)))
    if missing_nums:
        result = [missing_nums.pop()] + [nums]
    else:
        result = nums
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
