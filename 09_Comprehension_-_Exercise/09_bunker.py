"""
Using a comprehension, write a program that finds the number of given items in a bunker and their average quality.
On the first line, you will be given all item categories present in the bunker, then you will be given a
number (n). On the next "n" lines, you will be given different items in the following format:
"{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}"
Store that information, you will need it later. After you receive all the inputs, print the total amount of
items (sum the quantities) in the format:
"Count of items: {count}"
After that, print the average quality of all items in the following format, formatted to the second digit:
"Average quality: {quality sum/categories count}"
Finally, print all categories with the items on separate lines in the format:
"{category} -> {item1}, {item2}, …".
Input                               Output
food, water, materials, metal
5
food - pizza - quantity:10;quality:5
water - mineral - quantity:5;quality:10
materials - wood - quantity:2;quality:5
metal - copper - quantity:3;quality:10
food - burgers - quantity:5;quality:2

                                    Count of items: 25
                                    Average quality: 8.00
                                    food -> pizza, burgers
                                    water -> mineral
                                    materials -> wood metal -> copper
"""
bunker_items = {
    'food': {
        'pizza': {
            'quantity': 10,
            'quality': 5,
        },
        'burgers': {
            'quantity': 5,
            'quality': 2,
        },
    },
    'water': {
        'mineral': {
            'quantity': 2,
            'quality': 5,
        },
    },
    'materials': {
        'wood': {
            'quantity': 2,
            'quality': 5,
        },
    },
    'metal': {
        'copper': {
            'quantity': 3,
            'quality': 10,
        }
    },
}

print(bunker_items['food']['pizza']['quantity'])

for category in bunker_items:
    for kind in bunker_items[category]:
        for subdict in bunker_items[category][kind]:
            print(bunker_items[category][kind][subdict])


# bunker_items = {x: {} for x in input().split(', ')}

