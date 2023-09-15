"""
You will be given a start and an end. Print all the numbers in the given range (inclusive) that are divisible by any
of the numbers from 2 to 10. Use comprehensions for this problem.

Input   Output
1
20
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20]
45
50
        [45, 46, 48, 49, 50]
"""

start = int(input())
end = int(input())

result = [x for x in range(start, end + 1) if any(x % y == 0 for y in range(2, 11))]
print(result)
