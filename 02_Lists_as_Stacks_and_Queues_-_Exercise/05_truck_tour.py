"""
There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). For each
petrol pump, you will receive two pieces of information (separated by a single space):
- The amount of petrol the petrol pump will give you
- The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol
per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given
amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. You never
miss filling its tank at a petrol pump.
Input
    • On the first line, you will receive the number of petrol pumps - N
    • On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance
between that petrol pump and the next petrol pump, separated by a single space
Output
    • An integer which will be the smallest index of a petrol pump from which you can start the tour
Constraints
    • 1 ≤ N ≤ 1000001
    • 1 ≤ amount of petrol, distance ≤ 1000000000
    • You will always have at least one point from where the truck will be able to complete the circle
Input                   Output
3
1 5
10 3
3 4
                        1
5
22 5
14 10
52 7
21 12
36 9
                        0

7
4 3
3 4
10 7
3 14
22 5
12 2
13 1
                        4
8
6 15
10 1
10 1
6 12
10 1
6 6
6 6
10 5
6 12
                        0
"""
from collections import deque

gas_stations = int(input())


distance_queue = deque()
fuel_queue = deque()
station_idx = deque([int(x) for x in range(gas_stations)])

start_station = 0
for _ in range(gas_stations):
    fuel, distance = [int(x) for x in input().split()]
    distance_queue.append(distance)
    fuel_queue.append(fuel)

distance_stack = []
fuel_stack = []
petrol_in_tank = 0
while distance_queue:
    distance = distance_queue.popleft()
    fuel = fuel_queue.popleft()
    petrol_in_tank += fuel

    if petrol_in_tank >= distance:
        petrol_in_tank -= distance
        distance_stack.append(distance)
        fuel_stack.append(fuel)
    else:

        distance_queue.extend(distance_stack)
        fuel_queue.extend(fuel_stack)
        distance_stack = []
        fuel_stack = []
        petrol_in_tank = 0
    station_idx.rotate(-1)

print(station_idx.popleft())
