# from lab_works.basic_calcs import calculate_string
from lab_works.fibonacci import create_sequence, locate

# print(calculate_string('2.5 * 3'))



data = input()

command = input()
while command != 'Stop':
    data = data.split()
    number = int(data.pop())
    func = "_".join(data)
    

    command = input()
