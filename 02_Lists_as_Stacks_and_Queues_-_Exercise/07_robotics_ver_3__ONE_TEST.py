"""
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is
free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so
the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot
to take it, it should be queued at the end of the line again.
The robots are standing in line in the order of their appearance.
Input
• On the first line, you will receive the robots' names and their processing times in the format "robotNameprocessTime;robotName-processTime;robotName-processTime..."
• On the second line, you will get the starting time in the format "hh:mm:ss"
• Next, until the "End" command, you will get a product on each line.
Output
• Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

Input                           Output
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
                                ROB - detail [08:00:01]
                                SS2 - glass [08:00:02]
                                NX8000 - wood [08:00:03]
                                NX8000 - apple [08:00:06]

ROB-8
7:59:59
detail
glass
wood
sock
End
                                ROB - detail [08:00:00]
                                ROB - wood [08:00:08]
                                ROB - glass [08:00:16]
                                ROB - sock [08:00:24]

ROB-1
23:59:59
detail
glass
wood
sock
pepper
door
handle
matchbox
phone
rocket
keyboard
mouse
dominoes
chess
calculator
End
"""
from collections import deque
from datetime import datetime, timedelta

robots_raw_data = input().split(';')
robots_data = {}
robots_queue = deque()
for robot in robots_raw_data:
    name, busy_time = robot.split('-')
    robots_data[name] = timedelta(seconds=int(busy_time))
    robots_queue.append(name)

current_time = datetime.strptime(input(), '%H:%M:%S')

product = input()
product_queue = deque()
while product != 'End':
    product_queue.append(product)
    product = input()

available_at = {}
while product_queue:
    current_time += timedelta(seconds=1)
    current_product = product_queue.popleft()

    if current_time in available_at:
        robots_queue.extend(available_at[current_time])
        del available_at[current_time]

    if not robots_queue:
        product_queue.append(current_product)
    else:
        current_robot = robots_queue.popleft()
        print(f"{current_robot} - {current_product} [{current_time.strftime('%H:%M:%S')}]")
        time_available = current_time + robots_data[current_robot]
        if time_available not in available_at:
            available_at[time_available] = []
        available_at[time_available].append(current_robot)
