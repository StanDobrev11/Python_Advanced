"""
Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is
the sum of all ASCII values of that key.
Then, sort the dictionary:
 By values in descending order, if the sum of all values of the dictionary is odd
 By keys in ascending order, if the sum of all values of the dictionary is even
Note: Submit only the function in the judge system
Input
 There will be no input, just any number of words passed to your function
Output
 The function should return a string in the format "{key} ‐ {value}" for each key and value on a
separate lines
Constraints:
 There will be no case with capital letters.
 There will be no case with a string consisting of other than letters.

Test Code               Output                      Comment
print(
words_sorting(
'escape',
'charm',
'mythology'
))
                        charm ‐ 523
                        escape ‐ 625
                        mythology ‐ 1004
                                                    All of the ascii values of the 'escape' word are:
                                                    e = 101, s = 115, c = 99, a = 97, p = 112, e = 101
                                                    Their sum is 625.
                                                    We add it in the dictionary {'escape': 625}.
                                                    The ascii values of the 'charm' are:
                                                    c = 99, h = 104, a = 97, r = 117, m = 109
                                                    Their sum is 523.
                                                    We add it in the dictionary {'escape': 625, 'charm': 625}
                                                    The ascii values of the 'mythology' word are:
                                                    m = 109, y = 121, t = 116, h = 104, o = 111, l = 108, o = 111,
                                                    g = 103, y = 121.
                                                    Their sum is 1004.
                                                    We add it in the dictionary
                                                    {'escape': 625, 'charm': 523, 'mythology': 1004}
                                                    When we sum 625 + 523 + 1004 = 2152. The result is even,
                                                    and we sort the dictionary by keys in ascending order.
"""


def words_sorting(*args):
    def calculate_word_value():
        word_value = 0
        for letter in word:
            word_value += ord(letter)

        return word_value

    word_dict = {}
    ttl_value = 0
    for word in args:
        word_dict[word] = calculate_word_value()
        ttl_value += word_dict[word]

    if ttl_value % 2 == 0:
        word_dict = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        word_dict = sorted(word_dict.items(), key=lambda x: -x[1])

    return "\n".join(f'{k} - {v}' for k, v in word_dict)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
