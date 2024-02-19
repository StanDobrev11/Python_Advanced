from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

match_count = 0

while True:

    try:
        last_male = males[-1]
        first_female = females[0]

        if last_male <= 0 or first_female <= 0:

            if last_male <= 0:
                males.pop()

            if first_female <= 0:
                females.popleft()

            continue

        if last_male % 25 == 0 or first_female % 25 == 0:

            if last_male % 25 == 0:
                males.pop()
                last_male = males.pop()

            if first_female % 25 == 0:
                females.popleft()
                first_female = females.popleft()

            continue

        if last_male != first_female:
            last_male = males.pop() - 2
            males.append(last_male)
            females.popleft()
        else:
            males.pop()
            females.popleft()
            match_count += 1

    except IndexError:
        break

print(f"Matches: {match_count}")

if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
