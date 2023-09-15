"""
Write program that receives a list of characters and creates a dictionary with each character as a key and its
ASCII value as a value. Try solving that problem using comprehensions.
Input           Output

a, b, c, a
                {'a': 97, 'b': 98, 'c': 99}
d, c, m, h
                {'d': 100, 'c': 99, 'm': 109, 'h': 104}
"""


def read_data():
    return [x for x in input().split(', ')]


print({x: ord(x) for x in read_data()})
