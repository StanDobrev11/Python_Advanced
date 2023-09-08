"""
There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. When a
guest comes, check if they exist on any of the two reservation lists.
On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their
reservation codes. All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in
mind that all reservation numbers must be unique.
After that, you will be receiving guests who came to the party until you read the "END" command.
In the end, print the number of guests who did not come to the party and their reservation numbers:
• The VIP guests must be first.
• Both the VIP and the Regular guests must be sorted in ascending order.

Input       Output
5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END
            2
            7IK9Yo0h
            tSzE5t0p
6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END
            3
            7ugX7bm0
            UgffRkOn
            m8rfQBvl
"""
import tracemalloc

tracemalloc.start()


def read_input_to_list(count):
    input_set = set()
    for _ in range(count):
        input_set.add(input())
    return input_set


def guests_arrived(line_input, arrived: set) -> set:
    while not line_input == 'END':
        arrived.add(line_input)
        line_input = input()

    return arrived


def print_result(result):
    print(len(result))
    for el in result:
        print(el)


number_of_guests = int(input())

reservation_list = read_input_to_list(number_of_guests)
line = input()
guests_at_party = guests_arrived(line, set())
guests_not_arrived = guests_at_party.symmetric_difference(reservation_list)

print_result(sorted(guests_not_arrived))

print(tracemalloc.get_traced_memory())

tracemalloc.stop()
