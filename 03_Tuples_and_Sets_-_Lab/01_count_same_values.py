"""
You will be given numbers separated by a space. Write a program that prints the number of occurrences of each
number in the format "{number} - {count} times". The number must be formatted to the first decimal
point.

Input                                               Output
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
                                                    -2.5 - 3 times
                                                    4.0 - 2 times
                                                    3.0 - 4 times
                                                    -5.5 - 1 times
2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
                                                    2.0 - 3 times
                                                    4.0 - 6 times
                                                    5.0 - 4 times
                                                    3.0 - 7 times
"""
import time


# def my_count(values):
#     counted = {}
#     for item in values:
#         if item not in counted:
#             counted[item] = 1
#         else:
#             counted[item] += 1
#
#     return counted
#
#
# data = tuple(map(float, input().split()))
#
# start = time.time()
# for value, times in my_count(data).items():
#     print(f"{value} - {times} times")
# end = time.time()
# elapsed_time = end - start
# print(elapsed_time)  # 1.7664432525634766


# data = tuple(map(float, input().split()))
#
# start = time.perf_counter_ns()
# value_count = {}
# for value in data:
#     value_count[value] = data.count(value)
#
# for value, times in value_count.items():
#     print(f"{value} - {times} times")
#
# end = time.perf_counter_ns()
# elapsed_time = end - start
# print(elapsed_time) # 2.665867805480957

data = map(float, input().split())

start = time.perf_counter_ns()
counted = {}
for value in data:
    if value not in counted:
        counted[value] = 1
    else:
        counted[value] += 1

for value, times in counted.items():
    print(f"{value} - {times} times")

end = time.perf_counter_ns()
elapsed_time = end - start
print(elapsed_time) # 134600
