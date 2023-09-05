"""
You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is
one of these four types:
• '1 {number}' – push the number (integer) into the stack
• '2' – delete the number at the top of the stack
• '3' – print the maximum number in the stack
• '4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"


Input               Output
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4
                    26
                    20
                    91, 20, 26
10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4

                    32
                    66
                    8
                    8, 16, 25, 32, 66, 47
"""

operations = int(input())

stack = []
for _ in range(operations):
    command = input()
    if command.startswith('1'):
        stack.append(int(command.split()[1]))
    elif command == '2':
        try:
            stack.pop()
        except IndexError:
            continue
    elif command == '3':
        try:
            print(max(stack))
        except ValueError:
            continue
    elif command == '4':
        try:
            print(min(stack))
        except ValueError:
            continue


stack = [str(x) for x in stack]
print(', '.join(reversed(stack)))
