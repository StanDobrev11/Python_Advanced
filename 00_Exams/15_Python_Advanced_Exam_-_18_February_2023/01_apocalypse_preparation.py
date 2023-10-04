"""
You are in the middle of a zombie apocalypse and you want to go out for exploration. But before you do that, you
need to prepare some healing items.
On the first line, you will be given a sequence representing textiles. On the second line, you will be given another
sequence, which represents medicaments.
While both collections contain any elements, you will have to combine elements from the collections in order to
create healing items. You should start by getting the first value of textile and the last value of medicaments:
 If their sum is equal to any of the items in the table below create that item and remove both values.
 Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit, remove both values,
and add the remaining resources(of the sum) to the next value in the medicament collection (Take the
element from the collection, add the remaining sum to it, and put the element back to its place).
 If you can’t create anything, remove the textile value, add 10 to the medicament value, and return the
medicament back to its place, into its collection.
You need to stop creating healing items when either the textile or the medicaments are exhausted.
Healing item Resources needed
Patch 30
Bandage 40
MedKit 100
In the end, you should print on the console message for the sequence that has ended, then the created items, and in
the end the remaining items (if any).
Input
 On the first line, you will receive a sequence of integers representing the textiles, separated by a single
space (" ").
 On the second line, you will receive a sequence of integers representing the medicaments, separated by a
single space (" ").
Output
 On the first line print which one of the collections is over:
o If the textile is over print: "Textiles are empty."
o If the medicaments are over print: "Medicaments are empty."
o If both are empty print: "Textiles and medicaments are both empty."
 On the next n lines print only the created items (if any) ordered by the amount created descending, then
by name alphabetically:
"{item name} ‐ {amount created}
{item name} ‐ {amount created}
…
"
Hint: Do not print items, which are not created.
 On the last line print the remaining items(if any):
o If there are any medicaments left:
"Medicaments left: …{medicament2}, {medicament1}"
o If there are any textiles left:
"Textiles left: {textile1}, {textile2}…"
Constraints
 All the numbers will be in the range [0…1000].
 All the inputs will be valid.
Input           Output
20 10 40 70 20
10 50 10 30 20 80
                Textiles are empty.
                MedKit ‐ 2
                Bandage ‐ 1
                Patch ‐ 1
                Medicaments left: 50, 10
30 30 10 80 60
40 20 30 10 70
                Textiles and medicaments are both empty.
                MedKit ‐ 3
                Bandage ‐ 2
30 30 10 80 60 20
40 20 30 10 70
                Medicaments are empty.
                MedKit ‐ 3
                Bandage ‐ 2
                Textiles left: 20
60 15 20 30 20
20 15 40
                Medicaments are empty.
                Bandage ‐ 1
                MedKit ‐ 1
                Patch ‐ 1
                Textiles left: 30, 20
30 30 10 80 60 20
40 20 30 10 75
"""
from collections import deque


def start_crafting():
    while textiles and medicaments:
        combined = textiles[0] + medicaments[-1]

        if combined in medicine_mapper:
            if medicine_mapper[combined] not in items_crafted:
                items_crafted[medicine_mapper[combined]] = 0
            items_crafted[medicine_mapper[combined]] += 1
            textiles.popleft()
            medicaments.pop()

        elif combined > 100:
            if medicine_mapper[100] not in items_crafted:
                items_crafted[medicine_mapper[100]] = 0
            items_crafted[medicine_mapper[100]] += 1
            remaining = combined - 100
            textiles.popleft()
            medicaments.pop()

            try:
                medicaments[-1] += remaining
            except IndexError:
                medicaments.append(remaining)

        elif combined not in medicine_mapper:
            textiles.popleft()
            medicaments[-1] += 10


def print_outcome():
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")

    for key, value in sorted(items_crafted.items(), key=lambda x: (-x[1], x[0])):
        print(f"{key} - {value}")

    if medicaments:
        medicaments.reverse()
        print(f"Medicaments left: {', '.join(map(str, medicaments))}")
    if textiles:
        print(f"Textiles left: {', '.join(map(str, textiles))}")

    #
    #
    # if textiles:
    #     print(f"Textiles left: {', '.join(map(str, sorted(textiles, reverse=True)))}")
    # if medicaments:
    #     print(f"Medicaments left: {', '.join(map(str, sorted(medicaments, reverse=True)))}")


if __name__ == "__main__":
    medicine_mapper = {
        30: 'Patch',
        40: 'Bandage',
        100: 'MedKit',
    }
    items_crafted = {}
    textiles = deque(int(x) for x in input().split())
    medicaments = [int(x) for x in input().split()]
    start_crafting()
    print_outcome()
