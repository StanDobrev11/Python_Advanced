"""
First, you will receive a sequence of integers representing the materials for every wedding present. After that, you
will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.

Gift Magic needed
Gemstone 100 to 199
Porcelain Sculpture 200 to 299
Gold 300 to 399
Diamond Jewellery 400 to 499

To make a present, you should take the last integer of materials and sum it with the first magic level value. If the
result is between or equal to the numbers described in the table above, you make the corresponding gift and
remove both materials and magic value. Otherwise:
 If the product of the operation is under 100:
o And if it is an even number, double the materials, and triple the magic, then sum it again.
o And if it is an odd number, double the sum of the materials and the magic level. Then, check
again if it is between or equal to any of the numbers in the table above.
 If the product of the operation is more than 499, divide the sum of the material and the magic level
by 2. Then, check again if it is between or equal to any of the numbers in the table above.
 If, however, the result is not between or equal to any of the numbers in the table above after
performing the calculation, remove both the materials and the magic level.

Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs ‐ a gemstone and a
sculpture or gold and jewellery.
Input
 The first line of input will represent the values of materials ‐ integers, separated by a single space
 On the second line, you will be given the magic levels ‐ integers, separated by a single space
Output
 On the first line ‐ print whether you have succeeded in crafting the presents:
o "The wedding presents are made!"
o "Aladdin does not have enough wedding presents."
 On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
o "Materials left: {material1}, {material2}, …"
o "Magic left: {magicValue1}, {magicValue2}, …
 On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"

Constraints
 All the materials values will be integers in the range [1, 1000]
 Magic level values will be integers in the range [1, 1000]

Input                       Output                      Comment
105 20 30 25
120 60 11 400 10 1
                            The wedding presents are made!
                            Magic left: 10, 1
                            Gemstone: 1
                            Porcelain Sculpture: 2
                                                        First, we have 25 + 120 = 145, which is the needed
                                                        product for a gemstone. Remove both.
                                                        30 + 60 = 90 (under 100 and even) => 30 * 2 + 60
                                                        * 3 = 240 which is the needed product for a
                                                        porcelain sculpture. Remove both.
                                                        20 + 11 = 31 (under 100 and odd) => 31 * 2 = 62
                                                        which is under 100 again so we remove both.
                                                        105 + 400 = 505 (more than 450) => 505 / 2 =
                                                        252.5 which is the needed product for a diamond
                                                        porcelain sculpture. Remove both.
                                                        We do not have any material left. The program
                                                        ends. Print the desired text.
30 5 21 6 0 91
15 9 5 15 8
                            Aladdin does not have enough
                            wedding presents.
                            Materials left: 30
                            Gemstone: 1
200
5 15 32 20 10 5
                            Aladdin does not have enough
                            wedding presents.
                            Magic left: 15, 32, 20, 10, 5
                            Porcelain Sculpture: 1
"""
from collections import deque


def validate_sum(material, magic):
    value = material + magic
    if value < 100:
        if value % 2 == 0:  # double the materials, and triple the magic, then sum it again.
            value = material * 2 + magic * 3
        elif value % 2 == 1:  # And if it is an odd number, double the sum of the materials and the magic level.
            value *= 2
    elif value >= 500:  # divide the sum of the material and the magic level by 2
        value //= 2

    return value


def succeeded():
    if gifts_crafter['Gemstone'] > 0 and gifts_crafter['Porcelain Sculpture'] > 0:
        return True
    elif gifts_crafter['Gold'] > 0 and gifts_crafter['Diamond Jewellery'] > 0:
        return True
    return False


def print_result():
    if succeeded():
        print("The wedding presents are made!")
    else:
        print("Aladdin does not have enough wedding presents.")

    if materials:
        print(f"Materials left: {', '.join(map(str, materials))}")
    if magic_lvl:
        print(f"Magic left: {', '.join(map(str, magic_lvl))}")

    print(*[f"{key}: {value}\n" for key, value in sorted(gifts_crafter.items()) if value > 0])


materials = [int(x) for x in input().split()]
magic_lvl = deque(int(x) for x in input().split())

gifts_values = {
    range(100, 200): 'Gemstone',
    range(200, 300): 'Porcelain Sculpture',
    range(300, 400): 'Gold',
    range(400, 500): 'Diamond Jewellery',
}
gifts_crafter = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}

next_material = materials.pop()
next_magic_lvl = magic_lvl.popleft()

while True:

    sum_ = validate_sum(next_material, next_magic_lvl)

    for key, name in gifts_values.items():
        if sum_ in key:
            gifts_crafter[name] += 1
            break

    next_material, next_magic_lvl = 0, 0

    try:
        next_material = materials.pop()
        next_magic_lvl = magic_lvl.popleft()
    except IndexError:
        break

if next_material > 0:
    materials.append(next_material)
if next_magic_lvl > 0:
    magic_lvl.appendleft(next_magic_lvl)

print_result()
