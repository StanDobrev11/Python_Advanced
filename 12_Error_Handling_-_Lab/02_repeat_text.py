"""
Write a program that receives a text on the first line and times (to repeat the text) that must be an integer. If the
user passes a non-integer type for the times variable, handle the exception and print a message
"Variable times must be an integer".
Input       Output
Hello
Bye
            Variable times must be an integer
Hello
2
            HelloHello

"""

text = input()

while True:
    try:
        factor = int(input())
        print(text * factor)
        break
    except ValueError:
        print('Variable times must be an integer')



