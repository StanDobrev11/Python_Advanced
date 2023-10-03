"""
You will be given a sequence of 6 seats ‐ every seat is a mix of a number and a letter in the format
"{number}{letter}". You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence. Next,
take the sum of those two numbers and find its ASCII character.
 Compare each of the two taken numbers and the found character with the seats. If you find a match, the
passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
 If there is no equality, the two numbers should be returned at the end of their sequences (first becomes
last, last becomes first).
 If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep
track of all rotations made.
The program should end under the following circumstances:
 You have found 3 (three) seat matches
 You have made a total of 10 rotations
Input
 On the first line, you will be given a sequence of seats ‐ strings separated by comma and space ", "
 On the second and the third line, you will be given two more sequences ‐ integers separated by a comma
and a space ", "
Output
When the program ends, print the following on two different lines:
o Seat matches: {matches separated by comma and space}
o Rotations count: {total rotations made}
Constraints
 All integers will be in the range [1, 100]
 All letters will be in the range [A‐Z]
 You will never run out of numbers in your sequences before the program ends
 You will never have more than one match at a time
Input               Output
17K, 20B, 3C, 15D, 31Z, 28F
20, 35, 15, 3, 2, 10
1, 15, 64, 53, 45, 46
                    Seat matches: 20B, 15D, 3C
                    Rotations count: 4
25A, 16B, 44T, 49D, 27M, 44F
25, 3, 31, 49, 26, 13
10, 15, 44, 40
                    Seat matches: 25A, 44F
                    Rotations count: 10
15C, 25C, 36C, 43P, 40E, 38G
15, 25, 80, 40, 15, 99, 52
15, 42, 29
                    Seat matches: 25C, 40E, 15C
                    Rotations count: 7
"""
from collections import deque


def seats_taken_count():
    count = 0
    for seat, taken in seats.items():
        if taken:
            count += 1
    return count


def print_result(rotation_count, seats_taken):
    print(f"Seat matches: {', '.join(seats_taken)}")
    print(f"Rotations count: {rotation_count}")


def play():
    rotate_count = 0
    seats_taken = []
    while rotate_count < 10:

        try:
            sum_ = first_sequence[0] + second_sequence[-1]
        except IndexError:
            break

        ascii_chr = chr(sum_)
        potential_seats = [
            str(first_sequence[0]) + ascii_chr,
            str(second_sequence[-1]) + ascii_chr
        ]

        passenger_seated = False
        for seat in potential_seats:
            if seat in seats.keys():
                seats[seat] = True
                passenger_seated = True
                if seat not in seats_taken:
                    seats_taken.append(seat)

        if passenger_seated:
            first_sequence.popleft()
            second_sequence.pop()
        else:
            first_sequence.rotate(-1)
            second_sequence.rotate()

        rotate_count += 1

        if seats_taken_count() >= 3:
            break

    return rotate_count, seats_taken


if __name__ == "__main__":
    seats = {key: False for key in input().split(', ')}
    first_sequence = deque(int(x) for x in input().split(', '))
    second_sequence = deque(int(x) for x in input().split(', '))
    count, seats_taken = play()
    print_result(count, seats_taken)
