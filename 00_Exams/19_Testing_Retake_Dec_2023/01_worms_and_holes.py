from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

worms_count = len(worms)
matches_count = 0
while worms and holes:

    if worms[-1] == holes[0]:
        worms.pop()
        holes.popleft()
        matches_count += 1
        continue

    holes.popleft()
    worms[-1] -= 3
    if worms[-1] <= 0:
        worms.pop()

if matches_count > 0:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")

if not worms:
    if matches_count == worms_count:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    if worms_count > matches_count:
        print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
