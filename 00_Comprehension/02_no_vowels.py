"""
Using a comprehension write a program that receives a text and removes all the vowels from it, case-insensitive.
Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

Input       Output
Python
            Pythn
ILovePython
            LvPythn
"""

vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)

text = input()
print(''.join([x for x in text if x not in vowels]))
