"""
Rubber Duck Debugging is a type of debugging where you place a rubber duck on your desk and explain to it your
code line by line. You gathered a few programmers and gave them a task and judging by the time it took them to
write the code, you reward them with a type of rubber ducky.
Learn more about Rubber Duck Debugging after your exam from here.
You will be given two sequences of integers. The first one represents the time it takes a programmer to complete a
single task. The second one represents the number of tasks you’ve given to your programmers.
Your task is to count how many rubber ducks of each type you’ve given to your programmers.
While you have values in the sequences, you need to start from the first value of the programmers time's sequence
and multiply them by the last value of the tasks' sequence:
 If the calculated time is between any of the time ranges below, you give the corresponding ducky and
remove the programmer time's value and the tasks' value.
 If the calculated time goes above the highest range, decrease the number of the tasks' value by 2. Then,
move the programmer time's value to the end of its sequence, and continue with the next operation.
Rubber Ducky type Time needed to earn it
Darth Vader Ducky 0 ‐ 60
Thor Ducky 61 – 120
Big Blue Rubber Ducky 121 ‐ 180
Small Yellow Rubber
Ducky 181 ‐ 240
Your task is considered done when the sequences are empty.
Input
 The first line will represent each programmer’s time to complete a single task – integers, separated by a single
space.
 The second line will represent the number of tasks that should be completed – integers, separated by a single
space.
Output
 On the first line, you output:
o "Congratulations, all tasks have been completed! Rubber ducks rewarded:"
 On the next 4 lines, you output the type and number of ducks given, ordered like in the table:
o "Darth Vader Ducky: {count}
Thor Ducky: {count}
Big Blue Rubber Ducky: {count}
Small Yellow Rubber Ducky: {count}"
Constraints
 All the given numbers will be valid integers in the range [1, 1000].
 There will be no negative inputs.
 The number of values in both sequences will always be equal.
Input           Output
10 15 12 18 22 6
12 16 5 6 9 1
                Congratulations, all tasks have been
                completed! Rubber ducks rewarded:
                Darth Vader Ducky: 1
                Thor Ducky: 3
                Big Blue Rubber Ducky: 1
                Small Yellow Rubber Ducky: 1
2 55 17 31 23
7 5 17 4 27
                Congratulations, all tasks have been
                completed! Rubber ducks rewarded:
                Darth Vader Ducky: 1
                Thor Ducky: 0
                Big Blue Rubber Ducky: 2
                Small Yellow Rubber Ducky: 2
"""
from collections import deque


def start_to_work():

    while tasks_at_hand and time_required:

        calc_time = time_required[0] * tasks_at_hand[-1]
        for (start, end), duck in duck_mapper.items():
            if calc_time in range(start, end + 1):
                ducks_given[duck] += 1
                time_required.popleft()
                tasks_at_hand.pop()
                break

        else:
            time_required.rotate(-1)
            tasks_at_hand[-1] -= 2


def output():
    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
    for key, value in ducks_given.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    time_required = deque(int(x) for x in input().split())
    tasks_at_hand = deque(int(x) for x in input().split())

    duck_mapper = {
        (0, 60): 'Darth Vader Ducky',
        (61, 120): 'Thor Ducky',
        (121, 180): 'Big Blue Rubber Ducky',
        (181, 240): 'Small Yellow Rubber Ducky',
    }
    ducks_given = {
        'Darth Vader Ducky': 0,
        'Thor Ducky': 0,
        'Big Blue Rubber Ducky': 0,
        'Small Yellow Rubber Ducky': 0,
    }

    start_to_work()
    output()
