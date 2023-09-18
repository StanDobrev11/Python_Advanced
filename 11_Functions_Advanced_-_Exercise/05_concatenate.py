"""
Write a concatenate() function that receives some strings as arguments and some named arguments (the key
will be a string, and the value will be another string).
First, you should concatenate all arguments successively. Next, take each key successively, and if it is present in the
resulting string, change all matching parts with the key's value. In the end, return the final string.
See the examples for more clarification.
Submit only your function in the judge system

Test Code                                                Output
print(concatenate("Soft", "UNI", "Is", "Grate", "!",
UNI="Uni", Grate="Great"))
                                                        SoftUniIsGreat!
print(concatenate("I", " ", "Love", " ", "Cythons",
C="P", s="", java='Java'))
                                                        I Love Python
"""


def concatenate(*args, **kwargs):
    result_str = ''
    for string in args:
        result_str += string

    for key in kwargs:
        while key in result_str:
            idx = result_str.index(key)
            length = len(key)
            result_str = result_str[:idx] + kwargs[key] + result_str[idx + length:]
    return result_str


print(concatenate("Soft", "UNI", "Is", "Grate", "!",
                  UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons",
C="P", s="", java='Java'))