"""
The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice,
and they're going to have a really good time, but first, they have to get there. Even on his holiday trip, Sam is still
going to run into some problems, and the first one is getting to the airport. Right now, he is stuck in a traffic jam at a
crossroads where a lot of accidents happen.
Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed
the crossroads safely.
Sam is on a single lane of cars that queue until the light goes green. When it does, they start passing one by one on
a flashing green light and during the free window before the intersecting road's light goes green. For each second,
only one part of a car (a single character) passes the crossroad. If a car is still in the middle of the crossroads when
the free window ends, it will get hit at the first character that is still in the crossroads.
Input
    • On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
    • On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
    • On the following lines, until you receive the "END" command, you will receive one of two things:
        ▪ A car - a string containing the model of the car, or
        ▪ The command "green" that indicates the start of a green light cycle
A green light cycle goes as follows:
    • During the green light, cars will enter and exit the crossroads one by one
    • During the free window, cars will only exit the crossroads
Output
    • If a crash happens, end the program and print:
    "A crash happened!"
    "{car} was hit at {character_hit}."
    • If everything goes smoothly and you receive an "END" command, print:
    "Everyone is safe."
    "{total_cars_passed} total cars passed the crossroads."
    Constraints
    • The input will be within the constraints specified above and will always be valid. There is no need to check
    it explicitly.

Input               Output
10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END
                    Everyone is safe.
                    3 total cars passed the crossroads.

9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END
                    A crash happened!
                    Hummer was hit at e.

2
0
Mercedes
Hummer
green
Hummer
Mercedes
green
END
"""

from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

raw_input = input()
car_queue = deque()

car_stack = []
crashed_at = ''
is_crashed = False

while raw_input != 'END':
    enter_duration = green_light_duration
    exit_duration = free_window_duration
    all_passed = False
    if raw_input == 'green':
        car = car_queue.popleft()
        car_stack.append(car)
        car = deque(list(car))
        while car and not is_crashed:  # and enter_duration > 0 and exit_duration > 0:
            while enter_duration > 0:
                car.popleft()
                enter_duration -= 1
                if enter_duration > 0 and not car:
                    if car_queue:
                        car = car_queue.popleft()
                        car_stack.append(car)
                        car = deque(list(car))
                    else:
                        all_passed = True
                        break
            while exit_duration > 0 and not all_passed:
                if car:
                    car.popleft()
                    exit_duration -= 1
                else:
                    all_passed = True
                    break
            if car and exit_duration == 0:
                is_crashed = True
                crashed_at = car.popleft()
                break

    if is_crashed:
        break
    if raw_input != 'green':
        car_model = raw_input
        car_queue.append(car_model)
    raw_input = input()

if is_crashed:
    print('A crash happened!')
    print(f'{car_stack[-1]} was hit at {crashed_at}.')
else:
    print('Everyone is safe.')
    print(f'{len(car_stack)} total cars passed the crossroads.')
