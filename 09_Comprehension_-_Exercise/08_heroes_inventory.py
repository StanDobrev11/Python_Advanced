"""
Using a comprehension, write a program that receives a hero's names and items that need to be added in their inventory
(item name and item cost). Print the total amount of items with their total cost for each hero.
Input
    · On the first line, you will receive the names of the heroes separated by comma and space ", "
    · On the next lines until the command "End", you will be given items with their cost in the following format:
     "{name}-{item}-{cost}". If an item already exists in the hero's inventory - ignore it.
Output
    · For each hero, print his name, the total items and the total cost of the items in the format:
     "{name} -> Items: {items_count}, Cost: {items_cost}"
Input Output
Peter, George
Peter-Sword-20
Peter-Shield-10
George-Gem-100
Peter-Sword-15
George-Sword-20
End
                Peter -> Items: 2, Cost: 30
                George -> Items: 2, Cost: 120
"""

heroes = {x: {} for x in input().split(', ')}
items = {}
command = input()
while not command == 'End':
    name, item, value = command.split('-')
    if item not in heroes[name]:
        heroes[name][item] = int(value)
    command = input()

for hero in heroes:
    items_sum = 0
    for item in heroes[hero]:
        items_sum += heroes[hero][item]
    print(f'{hero} -> Items: {len(heroes[hero])}, Cost: {items_sum}')
