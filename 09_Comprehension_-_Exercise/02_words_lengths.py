"""
Using a list comprehension, write a program that receives some text, separated by comma and space ", ",
and prints on the console each string with its length in the following format:
"{first_str} -> {first_str_len}, {second_str} -> {second_str_len},…"

Input                               Output
Peter, George, Bill, Lilly, Katy
                                    Peter -> 5, George -> 6, Bill -> 4, Lilly -> 5, Katy -> 4
Some, Random, Text
                                    Some -> 4, Random -> 6, Text -> 4
"""


def output(word):
    return f'{word} -> {len(word)}'


text = input().split(', ')
text = [output(word) for word in text]
print(*text)
