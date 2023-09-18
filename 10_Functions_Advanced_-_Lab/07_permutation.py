"""
Write a program that reads a single string and prints all the possible combinations of the characters in that string.
Submit your solution in the judge system.
Input   Output

abc
        abc
        acb
        bac
        bca
        cba
        cab
"""


def permute(text, current_idx=0):
    if current_idx >= len(text):
        print(''.join(text))
        return
    for idx in range(current_idx, len(text)):
        text[current_idx], text[idx] = text[idx], text[current_idx]
        permute(text, current_idx + 1)
        text[current_idx], text[idx] = text[idx], text[current_idx]


text = list('1234')
permute(text)
