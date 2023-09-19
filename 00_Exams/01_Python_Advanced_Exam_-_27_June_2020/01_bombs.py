"""
You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of their values is
equal to any of the materials in the table below – create the bomb corresponding to the value and remove both
bomb materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you
have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
Bombs:
 Datura Bombs: 40
 Cherry Bombs: 60
 Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types.
Input
 On the first line, you will receive the integers representing the bomb effects, separated by ", ".
 On the second line, you will receive the integers representing the bomb casings, separated by ", ".
Output
 On the first line, print:
o if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the
bomb pouch!"
o if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill
the bomb pouch."
 On the second line, print all bomb effects left:
o If there are no bomb effects: "Bomb Effects: empty"
o If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
 On the third line, print all bomb casings left:
o If there are no bomb casings: "Bomb Casings: empty"
o If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
 Then, you need to print all bombs and the count you have of them, ordered alphabetically:
o "Cherry Bombs: {count}"
o "Datura Bombs: {count}"
o "Smoke Decoy Bombs: {count}"
Constraints
 All of the given numbers will be valid integers in the range [0, 120].
 There will be no cases with negative material.
Input               Output
5, 25, 25, 115
5, 15, 25, 35
                    You don't have enough materials to fill the bomb pouch.
                    Bomb Effects: empty
                    Bomb Casings: empty
                    Cherry Bombs: 0
                    Datura Bombs: 3
                    Smoke Decoy Bombs: 1
30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10
                    Bene! You have successfully filled
                    the bomb pouch!
                    Bomb Effects: 100, 80
                    Bomb Casings: 20
                    Cherry Bombs: 3
                    Datura Bombs: 4
                    Smoke Decoy Bombs: 3
"""
from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casing = [int(x) for x in input().split(', ')]

bomb_values = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}
bomb_count = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}


def check_quantity_of_bombs():
    for count in bomb_count.values():
        if count < 3:
            return False
    return True


has_finished = False
are_enough = False

while bomb_effects and bomb_casing:
    cur_effect = bomb_effects.popleft()
    cur_casing = bomb_casing.pop()
    comb_value = cur_effect + cur_casing
    while comb_value not in bomb_values:
        cur_casing -= 5
        comb_value = cur_effect + cur_casing
        if comb_value in bomb_values:
            continue
        if cur_casing == 0:
            if bomb_casing:
                cur_casing = bomb_casing.pop()
                comb_value = cur_effect + cur_casing
                continue
            else:
                break
    cur_bomb = bomb_values[comb_value]
    bomb_count[cur_bomb] += 1

    if check_quantity_of_bombs():
        are_enough = True
        break
    if not bomb_casing or not bomb_effects:
        has_finished = True
        break


if are_enough:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")
else:
    print("Bomb Casings: empty")

for bomb, count in sorted(bomb_count.items(), key=lambda x: x[0]):
    print(f"{bomb}: {count} ")
