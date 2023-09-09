"""
You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values
of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result
to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the
values of each set.
• If the sums of the two sets are equal, print the union of the values, separated by ", ".
• If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
separated by ", ".
• If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different
values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set

Input       Output              Comment
4
Pesho
Stefan
Stamat
Gosho
            304, 128, 206, 511
                                First name: Pesho. The sum of the ASCII values is: 80 + 101 + 115 + 104 +
                                111 = 511. Integer divide the sum to the current row (1): 511 / 1 = 511.
                                Second name: Stefan. The sum of the ASCII values is: 83 + 116 + 101 + 102
                                + 97 + 110 = 609. Integer divide the sum to the current row (2): 609 / 2 =
                                304.
                                Third name: Stamat. The sum of the ASCII values is: 83 + 116 + 97 + 109 +
                                97 + 116 = 618. Integer divide the sum to the current row (3): 618 / 3 = 206.
                                Fourth name: Gosho. The sum of the ASCII values is: 71 + 111 + 115 + 104
                                + 111 = 512. Integer divide the sum to the current row (4): 512 / 4 = 128.
                                The odd set: 511
                                The even set: 304, 206, 128
                                The sum of the even numbers is larger, so we print the symmetric-different
                                values.
6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan
            733, 101
"""


def read_input_to_list(count):
    input_set = []
    for _ in range(count):
        input_set.append(input())
    return input_set


def sum_of_ascii_chr(data):
    result = []
    for idx, item in enumerate(data):
        result_sum = 0
        for symbol in item:
            result_sum += ord(symbol)
        result_sum //= idx + 1
        result.append(result_sum)
    return result


def get_odd_even(data):
    odd = set()
    even = set()
    for number in data:
        if number % 2 == 0:
            even.add(number)
        else:
            odd.add(number)
    return even, odd


def compare_sum_of_values(even_set, odd_set):
    if sum(even_set) == sum(odd_set):
        return odd_set.union(even_set)
    elif sum(even_set) < sum(odd_set):
        return odd_set.difference(even_set)
    elif sum(even_set) > sum(odd_set):
        return odd_set.symmetric_difference(even_set)


def print_result(result):
    print(*result, sep=', ')


number_of_names = int(input())

set_of_names = read_input_to_list(number_of_names)
list_of_numbers = sum_of_ascii_chr(set_of_names)
even_set, odd_set = get_odd_even(list_of_numbers)
result_set = compare_sum_of_values(even_set, odd_set)
print_result(result_set)


c