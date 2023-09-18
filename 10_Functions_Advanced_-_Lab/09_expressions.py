"""
Write a program that generates all the possible expressions and their results between a given list of numbers using
only the + and - operators. Print them on the console as shown in the example
Input       Output

1, 1, 1, 1
            +1+1+1+1=4
            +1+1+1-1=2
            +1+1-1+1=2
            +1+1-1-1=0
            +1-1+1+1=2
            +1-1+1-1=0
            +1-1-1+1=0
            +1-1-1-1=-2
            -1+1+1+1=2
            -1+1+1-1=0
            -1+1-1+1=0
            -1+1-1-1=-2
            -1-1+1+1=0
            -1-1+1-1=-2
            -1-1-1+1=-2
            -1-1-1-1=-4
"""


def expressions(nums, current_sum=0, expression=''):
    if not nums:
        return [(expression, current_sum)]
    result_plus = expressions(nums[1:], current_sum + nums[0], expression + f"+{nums[0]}")
    result_minus = expressions(nums[1:], current_sum - nums[0], expression + f"-{nums[0]}")
    return result_plus + result_minus


data = [int(x) for x in input().split(' ')]

print(*[f"{el[0]}={el[1]}" for el in expressions(data)], sep='\n')
