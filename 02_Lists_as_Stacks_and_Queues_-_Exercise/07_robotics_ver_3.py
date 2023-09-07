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
