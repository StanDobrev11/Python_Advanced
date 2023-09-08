"""
Write a program that:
• Records a car number for every car that enters the parking lot
• Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines, you will receive the
direction and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or
"OUT". Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique. If
the parking lot is empty, print "Parking Lot is Empty".
Note: The order in which we print the result does not matter.

Input           Output

10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU
                CA2844AA
                CA9999TT
                CA2822UU
                CA9876HH
4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA

                Parking Lot is Empty
"""


def parking_validation(command, number, parking):
    if command == 'IN':
        parking.add(number)
    elif command == 'OUT':
        try:
            parking.remove(number)
        except KeyError:
            pass


def print_result(result):
    for el in result:
        print(el)


n = int(input())

cars_parked = set()
for _ in range(n):
    direction, car_plate = input().split(', ')
    parking_validation(direction, car_plate, cars_parked)

if cars_parked:
    print_result(cars_parked)
else:
    print('Parking Lot is Empty')
