"""
Create a function called rectangle(). It must have two parameters - length and width.
First, you need to check if the given arguments are integers:
· If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
Create two inner functions:
· area() - returns the area of the rectangle with the given length and width
· perimeter() - returns the perimeter of the rectangle with the given length and width
In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle
in the following format:
"Rectangle area: {ract_area}
Rectangle perimeter: {rect_perim}"

Test Code                   Output
print(rectangle(2, 10))
                            Rectangle area: 20
                            Rectangle perimeter: 24

print(rectangle('2', 10))
                            "Enter valid values!"
"""
from functools import reduce


def rectangle(*args):
    def is_integer(idx):
        if idx >= len(args):
            return True
        if not isinstance(args[idx], int):
            return False
        return is_integer(idx + 1)

    def area():
        return reduce(lambda x, y: x * y, args)

    def perimeter():
        return reduce(lambda x, y: (2 * x) + (2 * y), args)

    result = []
    if is_integer(0):
        result.append(f'Rectangle area: {area()}')
        result.append(f'Rectangle perimeter: {perimeter()}')
        return "\n".join(result)
    else:
        return "Enter valid values!"


print(rectangle(2, 10))
