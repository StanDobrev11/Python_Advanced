from collections import deque
from datetime import datetime, timedelta


class Robots:
    next_start_time = {}

    def __init__(self, name, process_time, order):
        self.name = name
        self.process_time = int(process_time)
        self.order = order
        self.next_start = 0

    def set_next_start(self, time):
        time += timedelta(seconds=self.process_time)
        if time not in Robots.next_start_time:
            Robots.next_start_time[time] = []
        Robots.next_start_time[time].append((self.name, self.order))
        return time


robots_data = input().split(';')
robots_queue = deque()
robots = {}
order = 0
for robot in robots_data:
    order += 1
    name, work_time = robot.split('-')
    robots[name] = Robots(name, work_time, order)
    robots_queue.append(name)

current_time = datetime.strptime(input(), '%H:%M:%S')

product = input()
product_queue = deque()
while product != 'End':
    product_queue.append(product)
    product = input()

while product_queue:
    current_time += timedelta(seconds=1)

    if current_time in Robots.next_start_time:
        for robot_name in sorted(Robots.next_start_time[current_time], key=lambda x: x[1]):
            robots_queue.append(robot_name[0])

    if robots_queue:
        product = product_queue.popleft()
        robot_name = robots_queue.popleft()
        print(f"{robot_name} - {product} [{current_time.strftime('%H:%M:%S')}]")
        robots[robot_name].next_start = robots[robot_name].set_next_start(current_time)
    else:
        product_queue.rotate(-1)
