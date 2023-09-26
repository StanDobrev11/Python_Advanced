"""
First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another
sequence of integers representing explosive power.
You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their
values is:
 divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
 divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
 divisible by both 3 and 5 – create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix
the same explosive power with the next firework effect.
If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
When you have successfully prepared enough fireworks for the show or you have no more firework punches or
explosive power, you need to stop mixing.
To make the perfect firework show, Maria needs 3 of each of the firework types.
Input
 On the first line, you will receive the integers representing the firework effects, separated by ", ".
 On the second line, you will receive the integers representing the explosive power, separated by ", ".
Output
 On the first line, print:
o if Maria successfully prepared the firework show: "Congrats! You made the perfect
firework show!"
o if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
 On the second line, print all firework effects left if there are any:
o "Firework Effects left: {effect1}, {effect2}, (…)"
 On the third line, print all explosive fillings left if there are any:
o " Explosive Power left: {filling1}, {filling2}, (…)"
 Then, you need to print all fireworks and the amount you have of them:
o "Palm Fireworks: {count}"
o "Willow Fireworks: {count}"
o "Crossette Fireworks: {count}"
Constraints
 All the given numbers will be integers in the range [‐100, 100].
 There will be no cases with empty sequences.

Input                                       Output
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
                                            Congrats! You made the perfect firework show!
                                            Palm Fireworks: 4
                                            Willow Fireworks: 3
                                            Crossette Fireworks: 3
-15, -8, 0, -16, 0, -22
10, 5
                                            Sorry. You can't make the perfect firework show.
                                            Explosive Power left: 10, 5
                                            Palm Fireworks: 0
                                            Willow Fireworks: 0
                                            Crossette Fireworks: 0
5, 6, 4, 16, 11, 5, -15, -8, 0, -16, 0, -22
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
"""
from collections import deque


def is_zero_or_negative(value):
    if value <= 0:
        return True
    return False


def check_fireworks(fireworks):
    return [False if value >= 3 else True for value in fireworks.values()]


effects = deque(int(x) for x in input().split(', '))
power = [int(x) for x in input().split(', ')]

fireworks = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0,
}
are_enough = False
current_effect = effects.popleft()
current_power = power.pop()
while True:

    if not any(check_fireworks(fireworks)):
        are_enough = True
        break

    try:
        while is_zero_or_negative(current_effect):
            current_effect = effects.popleft()

        while is_zero_or_negative(current_power):
            current_power = power.pop()
    except IndexError:
        break

    if (current_effect + current_power) % 3 == 0 and (current_effect + current_power) % 5 == 0:
        fireworks['Crossette'] += 1
        current_effect, current_power = 0, 0
    elif (current_effect + current_power) % 3 == 0:
        fireworks['Palm'] += 1
        current_effect, current_power = 0, 0
    elif (current_effect + current_power) % 5 == 0:
        fireworks['Willow'] += 1
        current_effect, current_power = 0, 0
    else:
        current_effect -= 1
        effects.append(current_effect)
        current_effect = effects.popleft()

    if not any(check_fireworks(fireworks)):
        are_enough = True
        break

if are_enough:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")
    if current_effect > 0:
        effects.appendleft(current_effect)
    if effects:
        print(f"Firework Effects left: {', '.join(map(str, effects))}")
    if current_power > 0:
        power.append(current_power)
    if power:
        print(f"Explosive Power left: {', '.join(map(str, power))}")

for k, v in fireworks.items():
    print(f"{k} Fireworks: {v}")
