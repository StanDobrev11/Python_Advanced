"""
Using a dictionary comprehension, write a program that receives country names on the first line,
separated by comma and space ", ", and their corresponding capital cities on the second line
(again separated by comma and space ", ") and prints each country, with their capital,
on a separate line in the following format:
"{country} -> {capital}"
Hints
· You can use the zip() method to zip the two lists into tuple pairs.
Input                                   Output
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London
                                        Bulgaria -> Sofia
                                        Romania -> Bucharest
                                        Germany -> Berlin
                                        England -> London
"""


def read_input():
    return input().split(', ')


def get_country_capital_pair(countries, capitals):
    return zip(countries, capitals)


def country_capital_list(zipped_object):
    return [f'{zipped_object[0]} -> {zipped_object[1]}' for zipped_object in zipped_object]


def print_output(combined_list):
    for item in combined_list:
        print(item)


countries = read_input()
capitals = read_input()
zipped = get_country_capital_pair(countries, capitals)
combined_list = country_capital_list(zipped)
print_output(combined_list)
