"""
You are given an algebraic expression with parentheses. Scan through the string and extract each set of
parentheses.
Print the result back on the console.
Examples
Input                                   Output
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5     (2 + 3)
                                        (3 + 1)
                                        (2 - (2 + 3) * 4 / (3 + 1))
(2 + 3) - (2 + 3)                       (2 + 3)
                                        (2 + 3)
"""

equation = list(input())
stack = []
for idx in range(len(equation)):
    if equation[idx] == '(':
        stack.append(idx)
    elif equation[idx] == ')':
        start_idx = stack.pop()
        end_idx = idx
        print("".join(equation[start_idx:end_idx + 1]))
