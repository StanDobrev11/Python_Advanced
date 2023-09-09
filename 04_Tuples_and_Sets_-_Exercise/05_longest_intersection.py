"""
Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you
will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}".
You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its
length in the format: "Longest intersection is [{longest_intersection_numbers}] with length
{length_longest_intersection}"
Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one

Input           Output                                  Comment
3
0,3-1,2
2,10-3,5
6,15-3,10
                Longest intersection is [6, 7, 8, 9,
                10] with length 5
                                                        The intersection of [0-3] and [1-2] is [1-2]
                                                        (length 2)
                                                        The intersection of [2-10] and [3-5] is [3-5]
                                                        (length 3)
                                                        The intersection of [6-15] and [3-10] is [6-10]
                                                        (length 5) - which is the longest
5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11
                Longest intersection is [2, 3, 4, 5, 6,
                7, 8, 9, 10] with length 9
"""
from collections import deque


def split_input_by_dash(count):
    lines = []
    for _ in range(count):
        line = input().split('-')
        lines.append(line)
    return lines


def split_by_coma(lines):
    index_list = []
    for item in lines:
        for value in item:
            start_idx, end_idx = [int(x) for x in value.split(',')]
            index_list.append((start_idx, end_idx))
    return index_list


def find_sets_by_start_end_idx(data):
    queue = deque()
    for item in data:
        next_set = set()
        start_idx, end_idx = item
        for num in range(start_idx, end_idx + 1):
            next_set.add(num)
        queue.append(next_set)
    return queue


def find_intersection(data):
    intersections = dict()
    while data:
        first_set = data.popleft()
        second_set = data.popleft()
        result_intersection = first_set.intersection(second_set)
        intersections[len(result_intersection)] = result_intersection
    return intersections


def print_result(result_dict):
    max_len = max(result_dict)
    max_set = result_dict[max_len]
    max_set_str = map(str, max_set)
    print(f"Longest intersection is [{', '.join(max_set_str)}] with length {max_len}")


number_of_lines = int(input())

lines_split_by_dash = split_input_by_dash(number_of_lines)
list_start_end_idx = split_by_coma(lines_split_by_dash)
queue_sets = find_sets_by_start_end_idx(list_start_end_idx)
dict_of_intersections = find_intersection(queue_sets)
print_result(dict_of_intersections)
