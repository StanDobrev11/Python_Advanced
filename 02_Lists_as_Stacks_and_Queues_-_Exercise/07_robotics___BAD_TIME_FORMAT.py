from collections import deque
import datetime


robots = input().split(';')
robots_process_time = {}
robots_in_queue = deque()
for robot in robots:
    name, process_time = robot.split('-')
    robots_process_time[name] = int(process_time)
    robots_in_queue.append(name)

h, m, s = [int(x) for x in input().split(':')]
start_time = datetime.timedelta(hours=h, minutes=m, seconds=s)

seconds_lapsed = 0
detail_queue = deque()
detail = input()
robots_next_start = {}
while not detail == 'End':
    detail_queue.append(detail)
    detail = input()

while detail_queue:
    seconds_lapsed += 1
    seconds_as_delta = datetime.timedelta(seconds=seconds_lapsed)
    current_time = start_time + seconds_as_delta

    if current_time in robots_next_start.keys():
        for name in robots_next_start[current_time]:
            robots_in_queue.append(name)

    if robots_in_queue:
        name = robots_in_queue.popleft()
        print(f'{name} - {detail_queue.popleft()} [{"{:0>8}".format(str(current_time))}]')
        robot_work_time = datetime.timedelta(seconds=robots_process_time[name])
        next_start = datetime.timedelta(seconds=current_time.total_seconds()) + robot_work_time
        if next_start not in robots_next_start:
            robots_next_start[next_start] = []
        robots_next_start[next_start].append(name)

    else:
        detail_queue.rotate(-1)

# ROB - detail [1 day, 0:00:00]
# JOHNY - glass [1 day, 0:00:01]
# ASEN - wood [1 day, 0:00:02]
# ASEN - pepper [1 day, 17:34:16]
# ROB - handle [1 day, 20:56:53]
# ASEN - chess [2 days, 11:08:30]
# ROB - keyboard [2 days, 17:53:46]
# ASEN - dominoes [3 days, 4:42:44]
# ROB - phone [3 days, 14:50:39]
# ASEN - rocket [3 days, 22:16:58]
# ROB - door [4 days, 11:47:32]
# ASEN - sock [4 days, 15:51:12]
# ROB - matchbox [5 days, 8:44:25]
# ASEN - mouse [5 days, 9:25:26]
# ASEN - calculator [6 days, 2:59:40]