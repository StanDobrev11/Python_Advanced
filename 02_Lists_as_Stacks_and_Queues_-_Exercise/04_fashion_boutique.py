"""
You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers.
In the following line, you will be given an integer representing the capacity for one rack in your store.
You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last
piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. Each piece of
clothing has its value (an integer). You must sum their values while you take them out of the box:
    • If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes
    (if there are any left in the box).
    • If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a
new rack and then hang it up.
In the end, print how many racks you have used to hang up the clothes.
Input
    • On the first line, you will be given a sequence of integers representing the clothes in the box, separated by a
single space.
    • On the second line, you will be given an integer representing the capacity of a rack.
Output
    • Print the number of racks needed to hang up the clothes from the box.

Input                           Output
5 4 8 6 3 8 7 7 9
16
                                5
1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20
                                5
"""
clothes_by_weight = [int(x) for x in input().split()]
rack_max_load = int(input())

rack_current_load = 0
racks_used = 0
while clothes_by_weight:
    next_cloth = clothes_by_weight.pop()
    # if rack_current_load + next_cloth > rack_max_load:
    #     rack_current_load = 0
    #     racks_used += 1
    # elif rack_current_load + next_cloth == rack_max_load:
    #     rack_current_load = 0
    #     racks_used += 1
    #     continue
    # rack_current_load += next_cloth
    if rack_current_load + next_cloth <= rack_max_load:
        rack_current_load += next_cloth
    else:
        rack_current_load = next_cloth
        racks_used += 1


if rack_current_load > 0:
    racks_used += 1

print(racks_used)
