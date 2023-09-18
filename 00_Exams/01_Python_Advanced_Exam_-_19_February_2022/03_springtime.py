"""
Write a function called start_spring which will receive a different number of keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value holds its type (string). For
example, dahlia="flower", shrikes="bird", dogwood="tree".
The function should sort the given spring objects in collections by their type:
 The collections sorted by their number of elements in descending order. If two or more collections have
the same number of elements in them, return them in ascending order (alphabetically) by the type's name.
 Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
Note: Submit only the function in the judge system

            flower:
            ‐Dahlia
            ‐Tulip
            ‐Water Lilly
            bird:
            ‐Swallows
            ‐Swifts
            tree:
            ‐Callery Pear
"""


def start_spring(**kwargs):
    value_count = {}
    for key, value in kwargs.items():
        if value not in value_count:
            value_count[value] = 0
        value_count[value] += 1
    result = {}
    value_count = dict(sorted(value_count.items(), key=lambda x: -x[1]))
    for type_ in value_count.keys():
        if type_ not in result:
            result[type_] = []
        for key, value in kwargs.items():
            if type_ == value:
                result[type_].append(key)

    resss = []
    for key, values in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        word = key + ':'
        resss.append(word)
        for value in sorted(values):
            word = '-' + value
            resss.append(word)

    return '\n'.join(resss)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}

print(start_spring(**example_objects))
