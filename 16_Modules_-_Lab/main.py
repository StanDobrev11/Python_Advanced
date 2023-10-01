# from lab_works.basic_calcs import calculate_string
from lab_works.fibonacci import create_sequence, locate

# print(calculate_string('2.5 * 3'))

seq = []
command = input()
while command != 'Stop':

    data = command.split()
    if data[0].lower() == 'create':
        count = int(data[-1])
        seq = create_sequence(count)
        print(' '.join(map(str, seq)))

    elif data[0].lower() == 'locate':
        number = int(data[-1])
        print(locate(number, seq))

    command = input()
