"""
You will receive a list of the customers (numbers separated by comma and space ", ") on the first line and list of
your taxis (numbers separated by comma and space ", ").
Each number from the customer list represents how much time it takes to drive the customer to his/her
destination.
Each number from the taxis list represents how much time they can drive, before they need to refill their tanks.
Keep track of the total time passed to drive all the customers to their destinations (values of all customers).
Each time you tend customers you should put the first customer in the last taxi until there are no customers left.
 If the taxi can drive the customer to his/her destination, he does and you must add the time passed to
drive the customer to his/her destination (the value of the current customer) to the total time. Remove
both the customer and the taxi.
 If the taxi cannot drive the customer to his/her destination, leave the customer at the beginning of the
queue and remove the taxi.
At the end if you have successfully driven all the customers to their destinations, print
All customers were driven to their destinations
Total time: {total_time} minutes
Otherwise, if you ran out of taxis and there are still some customers left print
Not all customers were driven to their destinations
Customers left: {left_customers joined by ", "}
Input
 On the first line you are given the customers – numbers separated by comma and space ", "
 On the second line you are given the taxis – numbers separated by comma and space ", "
Output
 Print the output as described above
Constraints
 You will always have at least one customer and at least one taxi

Input                               Output
4, 6, 8, 5, 1
1, 9, 15, 10, 6
                                    All customers were driven to their destinations
                                    Total time: 24 minutes
10, 5, 8, 9
2, 4, 5, 8
                                    Not all customers were driven to their destinations
                                    Customers left: 10, 5, 8, 9
2, 8, 4, 3, 11, 7
10, 15, 4, 6, 3, 10, 2, 1
                                    All customers were driven to their destinations
                                    Total time: 35 minutes
"""
from collections import deque

passengers = deque(int(x) for x in input().split(', '))
taxis = [int(x) for x in input().split(', ')]

total_time = 0
while taxis and passengers:
    time_available = taxis.pop()
    time_required = passengers.popleft()
    while time_available < time_required:
        if taxis:
            time_available = taxis.pop()
        else:
            passengers.appendleft(time_required)
            break
    total_time += time_required
    time_available = 0
    time_required = 0
    if not taxis or not passengers:
        break

if not passengers:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, passengers))}')
