"""
Write a recursive function called palindrome() that will receive a word and an index (always 0). Implement the
function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a
palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.

print(palindrome("abcba", 0)) abcba is a palindrome
print(palindrome("peter", 0)) peter is not a palindrome
"""


def palindrome(word, idx):
    if word[idx] != word[-idx - 1]:
        return f"{word} is not a palindrome"

    if len(word) // 2 == idx:
        return f"{word} is a palindrome"

    return palindrome(word, idx + 1)


print(palindrome("adasdadasdad", 0))
print(palindrome("abcba", 0))
print(palindrome("koraVVarok", 0))
