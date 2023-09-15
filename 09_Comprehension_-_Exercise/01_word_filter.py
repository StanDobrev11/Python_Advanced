"""
Using a comprehension, write a program that receives some text, separated by space, and take only those words,
whose length is even. Print each word on a new line.

Input                       Output
kiwi orange banana apple
                            kiwi orange banana
pizza cake pasta chips
                            cake
"""


def even_length(word):
    return len(word) % 2 == 0


text = input().split()
text = [word for word in text if even_length(word)]
print(*text)
