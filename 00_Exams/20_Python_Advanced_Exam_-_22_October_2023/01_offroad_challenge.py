from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_idx = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

altitude_reached = 0
while True:

    try:
        fuel = initial_fuel.pop()
        add_con_idx = additional_consumption_idx.popleft()

    except IndexError:
        break

    if fuel - add_con_idx >= fuel_needed[0]:
        fuel_needed.popleft()
        altitude_reached += 1
        print(f"John has reached: Altitude {altitude_reached}")

    else:
        print(f"John did not reach: Altitude {altitude_reached + 1}")
        break

if altitude_reached == 0:
    print("John failed to reach the top.\n"
          "John didn't reach any altitude.")

elif altitude_reached > 0:
    if fuel_needed:

        result = []
        for alt in range(altitude_reached):
            result.append(f'Altitude {alt + 1}')

        print(f"John failed to reach the top.\n"
              f"Reached altitudes: {', '.join(result)}")

    else:
        print("John has reached all the altitudes and managed to reach the top!")
