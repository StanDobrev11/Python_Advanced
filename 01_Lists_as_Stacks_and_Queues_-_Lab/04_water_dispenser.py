"""
Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines,
you will be given the names of some people who want to get water (each on a separate line) until you receive the
command "Start". Add those people to a queue. Finally, you will receive some commands until the command
"End":
- "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough
water in the dispenser for that person.
o If there is enough water, print "{person_name} got water" and remove him/her from the
queue.
o Otherwise, print "{person_name} must wait" and remove the person from the queue without
reducing the water in the dispenser.
- "refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left"

Input                   Output                  Comment
2
Peter
Amy
Start
2
refill 1
1
End
                        Peter got water
                        Amy got water
                        0 liters left
                                                We create a queue with Peter and Amy. After the start
                                                command, we see that Peter wants 2 liters of water (and
                                                he gets them). The water dispenser is left with 0 liters.
                                                After refilling, there is 1 liter in the dispenser. So when
                                                Amy wants 1 liter, she gets it, and there are 0 liters left in
                                                the dispenser.
"""
from collections import deque

quantity_of_water = int(input())

queue = deque()
name = input()
while not name == 'Start':
    queue.append(name)
    name = input()

command = input()
while not command == 'End':
    command = command.split()
    if command[0] == 'refill':
        litters = int(command[1])
        quantity_of_water += litters
    else:
        litters = int(command[0])
        if quantity_of_water - litters >= 0:
            quantity_of_water -= litters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{quantity_of_water} liters left")
