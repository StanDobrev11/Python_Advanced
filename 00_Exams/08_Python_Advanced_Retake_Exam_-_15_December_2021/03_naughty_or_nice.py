"""
Write a function called naughty_or_nice_list which will receive
 A list representing Santa Claus' "Naughty or Nice" list full of kids' names
 A different number of arguments (strings) and/or keywords representing commands
The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids ‐ tuples containing two elements: a counting number (integer) at the first
position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords.
Each argument is a command. The commands could be the following:
 "{counting_number}‐Naughty" ‐ if there is only one tuple in the given list with the same number,
MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the
command.
 "{counting_number}‐Nice" ‐ if there is only one tuple in the given list with the same number, MOVE
the kid to a list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
 If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE
kids depending on the value in the keyword. Then, remove it from the Santa list.
 Otherwise, ignore the command.
All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found"
list.
In the end, return the final lists, each on a new line as described below.
Note: Submit only the function in the judge system
Input
 There will be no input. Just parameters passed to your function.
Output
 The function should return strings with the names on each list on separate lines, if there are any,
otherwise skip the line:
o "Nice: {name1}, {name2} … {nameN}"
o "Naughty: {name1}, {name2} … {nameN}"
o "Not found: {name1}, {name2} … {nameN}"
print(naughty_or_nice_list(
[
(3, "Amy"),
(1, "Tom"),
(7, "George"),
(3, "Katy"),
],
"3‐Nice",
"1‐Naughty",
Amy="Nice",
Katy="Naughty",
))
                    Nice: Amy
                    Naughty: Tom, Katy
                    Not found: George
print(naughty_or_nice_list(
[
(7, "Peter"),
(1, "Lilly"),
(2, "Peter"),
(12, "Peter"),
(3, "Simon"),
],
"3‐Nice",
"5‐Naughty",
"2‐Nice",
"1‐Nice",
))
                    Nice: Simon, Peter, Lilly
                    Not found: Peter, Peter
print(naughty_or_nice_list(
[
(6, "John"),
(4, "Karen"),
(2, "Tim"),
(1, "Merry"),
(6, "Frank"),
],
"6‐Nice",
"5‐Naughty",
"4‐Nice",
"3‐Naughty",
"2‐Nice",
"1‐Naughty",
Frank="Nice",
Merry="Nice",
John="Naughty",
))
                    Nice: Karen, Tim, Frank
                    Naughty: Merry, John
"""


def naughty_or_nice_list(santas_list, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    list_by_number = []
    list_by_names = []

    for item in santas_list:
        list_by_number.append(item[0])
        list_by_names.append(item[1])

    for item in args:

        try:
            index = list_by_number.index(int(item.split('-')[0]))
            if list_by_number.count(int(item.split('-')[0])) >= 2:
                raise ValueError
        except ValueError:
            continue

        if item.split('-')[1] == 'Nice':
            nice.append(list_by_names[index])
        else:
            naughty.append(list_by_names[index])

    for key, value in kwargs.items():
        if list_by_names.count(key) >= 2:
            continue
        if value == 'Nice':
            if key not in naughty:
                nice.append(key)
        else:
            if key not in nice:
                naughty.append(key)

    for name in list_by_names:
        if name not in nice and name not in naughty:
            not_found.append(name)

    result = print_(nice, naughty, not_found)

    return result


def print_(nice, naughty, not_found):
    result_text = ''
    if nice:
        result_text += f"Nice: {', '.join(x for x in nice)}\n"
    if naughty:
        result_text += f"Naughty: {', '.join(x for x in naughty)}\n"
    if not_found:
        result_text += f"Not found: {', '.join(x for x in not_found)}\n"

    return result_text


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
