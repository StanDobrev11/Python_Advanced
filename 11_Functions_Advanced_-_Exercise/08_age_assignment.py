"""
Create a function called age_assignment() that receives a different number of names and a different number of
key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number (age). Find its
first letter in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line
in the format: "{name} is {age} years old."
Submit only the function in the judge system.
Test Code                   Output
print(age_assignment("Peter", "George", G=26, P=19))
                            George is 26 years old.
                            Peter is 19 years old.
print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))
                            Amy is 22 years old.
                            Bill is 61 years old.
                            Willy is 36 years old.
"""


def age_assignment(*names, **ages):
    result = []
    for name in sorted(names):
        age = ages[name[0]]
        result.append(f'{name} is {age} years old.')

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36,
                     A=22, B=61))
