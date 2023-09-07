"""
Our favorite super-spy action hero Sam is back from his vacation, and it is time to go on a mission. He needs to
unlock a safe locked by several locks in a row, which all have varying sizes.
The hero possesses a special weapon called the Key Revolver, with special bullets. Each bullet can unlock a lock with
a size equal to or larger than the size of the bullet. The bullet goes into the keyhole, then explodes, completely
destroying it. Sam doesn't know the size of the locks, so he needs to just shoot at all of them until the safe runs out
of locks.
What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, keeps his topsecret Georgian Chacha Brandy recipe inside. It's valued differently across different times of the year, so Sam's boss
will tell him what it's worth over the radio. One last thing, every bullet Sam fires will also cost him money, which will
be deducted from his pay from the price of the intelligence.
Good luck, operative.
Input
    • On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
    • On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
    • On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
    • On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
    • On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
Output
    • If Sam manages to open the safe, print:
    "{bullets_left} bullets left. Earned ${money_earned}"
    • Otherwise, print:
    "Couldn't get through. Locks left: {locks_left}"
    Make sure to include the price of the bullets when calculating the money earned.
Constraints
    • The input will be within the constraints specified above and will always be valid. There is no need to check
    it explicitly.
    • There will never be a case where Sam breaks the lock and ends up with а negative balance.
Input                           Output                              Comments
50
2
11 10 5 11 10 20
15 13 16
1500
                                Ping!                               20 shoots lock 15 (ping)
                                Bang!                               10 shoots lock 15 (bang)
                                Reloading!                          11 shoots lock 13 (bang)
                                Bang!                                5 shoots lock 16 (bang)
                                Bang!                               Bullets' cost: 4 * 50 = $200
                                Reloading!                          Earned: 1500 – 200 = $1300
                                2 bullets left. Earned $1300
20
6
14 13 12 11 10 5
13 3 11 10
800
                                Bang!
                                Ping!
                                Ping!
                                Ping!
                                Ping!
                                Ping!
                                Couldn't get through. Locks left: 3

50
2
1 11 10 5 11 10 20 18 17 23 15 16
20
1500
                                Bang!
                                11 bullets left. Earned $1450
"""
from collections import deque


def load_gun(barrel_size, bullets_size):
    barrel = deque()
    if len(bullets_size) >= barrel_size:
        for _ in range(barrel_size):
            barrel.append(bullets_size.pop())
    else:
        while bullets_size:
            barrel.append(bullets_size.pop())
    return barrel


bullet_cost = int(input())
barrel_size = int(input())

bullets_size = deque(int(x) for x in input().split())
locks_size = deque(int(x) for x in input().split())
bullets_count = len(bullets_size)

value_of_intelligence = int(input())
barrel = load_gun(barrel_size, bullets_size)

if bullets_size or barrel:
    has_bullets = True
else:
    has_bullets = False

bullets_used = 0
while locks_size and has_bullets:
    if barrel:
        shot_size = barrel.popleft()
        bullets_used += 1
        if shot_size <= locks_size[0]:
            print('Bang!')
            locks_size.popleft()
        else:
            print('Ping!')
    else:
        if bullets_size:
            barrel = load_gun(barrel_size, bullets_size)
            print('Reloading!')
        else:
            has_bullets = False
            break

if locks_size:
    print(f"Couldn't get through. Locks left: {len(locks_size)}")
else:
    cost = value_of_intelligence - (bullets_used * bullet_cost)
    if len(bullets_size) > 0 and len(barrel) == 0:
        print('Reloading!')
    print(f'{len(bullets_size) + len(barrel)} bullets left. Earned ${cost}')
