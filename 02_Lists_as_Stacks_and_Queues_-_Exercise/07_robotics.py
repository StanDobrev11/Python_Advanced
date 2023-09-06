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
mango
rocket
wool
eggs
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
"""

import datetime
from collections import deque

robots = input().split(';')
robots_process_time = {}
robots_in_queue = deque()
for robot in robots:
    name, process_time = robot.split('-')
    robots_process_time[int(process_time)] = name
    robots_in_queue.append(name)

h, m, s = [int(x) for x in input().split(':')]
start_time = datetime.timedelta(hours=h, minutes=m, seconds=s)

seconds_lapsed = 0
detail_queue = deque()
detail = input()
while not detail == 'End':
    detail_queue.append(detail)
    while detail_queue:
        seconds_lapsed += 1
        for time, name in robots_process_time.items():
            if seconds_lapsed % time == 0 and name not in robots_in_queue:
                robots_in_queue.append(name)

        if robots_in_queue:
            seconds_as_delta = datetime.timedelta(seconds=seconds_lapsed)
            current_time = start_time + seconds_as_delta
            print(f'{robots_in_queue.popleft()} - {detail_queue.popleft()} [{current_time}]')

    detail = input()
