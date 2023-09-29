"""
Create a function named flights that receives a different number of arguments representing the information
about the flights for a day:
 the destination of each flight
 the count of passengers that are boarding the plane
 a string "Finish"
You need to take each argument and make a dictionary with the plane’s destination as a key and the passengers as
a value of the corresponding key.
If there are more than one flight to the same destination, you should count all the passengers that flew to the
destination.
You should modify the dictionary until the current argument is equal to "Finish".
Note: Submit only the function in the judge system
Input
 There will be no input, just parameters passed to your function
Output
 The function should return the final dictionary
Constrains
 All numbers will be valid integers in the range [0, 300]

test code                       output
print(flights('Vienna', 256, 'Vienna', 26,
'Morocco', 98, 'Paris', 115, 'Finish',
'Paris', 15))
                                {'Vienna': 282, 'Morocco': 98, 'Paris':
                                115}
print(flights('London', 0, 'New York', 9,
'Aberdeen', 215, 'Sydney', 2, 'New York',
300, 'Nice', 0, 'Finish'))
                                {'London': 0, 'New York': 309,
                                'Aberdeen': 215, 'Sydney': 2, 'Nice': 0}
print(flights('Finish', 'New York', 90,
'Aberdeen', 300, 'Sydney', 0))
                                {}
"""
from collections import deque


def flights(*args):
    list_of_flights = deque(args[:args.index('Finish')])
    daily_flights = {}
    while list_of_flights:
        destination = list_of_flights.popleft()
        passengers = int(list_of_flights.popleft())
        if destination not in daily_flights:
            daily_flights[destination] = 0
        daily_flights[destination] += passengers

    return daily_flights


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9,
'Aberdeen', 215, 'Sydney', 2, 'New York',
300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90,
'Aberdeen', 300, 'Sydney', 0))