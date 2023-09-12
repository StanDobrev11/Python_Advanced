"""
Write a program to flatten several lists of numbers received in the following format:
▪ String with numbers or empty strings separated by "|"
▪ Values are separated by spaces (" ", one or several)
▪ Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
Input               Output
1 2 3 |4 5 6 | 7 88
                    7 88 4 5 6 1 2 3
7 | 4 5|1 0| 2 5 |3
                    3 2 5 1 0 4 5 7
1| 4 5 6 7 | 8 9
                    8 9 4 5 6 7 1
"""

lists = [x.strip() for x in input().split('|')]

new_list = []
for lst in lists:
    new_lst = lst.split()
    new_list.append(new_lst)

final_list = []
for lst in range(len(new_list) - 1, -1, -1):
    final_list.extend(new_list[lst])

print(*final_list)
