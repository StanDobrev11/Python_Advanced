"""
Write a function called fill_the_box that receives a different number of arguments representing:
• the height of a box
• the length of a box
• the width of a box
• different numbers - each representing the quantity of cubes. Each cube has an exact size of 1 x 1 x 1
• a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Note: Submit only the function in the judge system
Input
• There will be no input. Just parameters passed to your function.
Output
The function should return a string in the following format:
• If, in the end, there is free space left in the box, print:
o "There is free space in the box. You could put {free space in cubes} more
cubes."
• If there is no free space in the box, print:
o "No more free space! You have {cubes left} more cubes."

Test Code                       Output                          Comment
print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))
                                There is free space in
                                the box. You could put 13
                                more cubes.
                                                                The size of the box: 2 * 8 * 2 = 32
                                                                We put the cubes consistently. In the
                                                                end, there is more free space left.
print(fill_the_box(5, 5,
2, 40, 11, 7, 3, 1, 5,
"Finish"))
                                No more free space! You
                                have 17 more cubes.
                                                                The size of the box: 5 * 5 * 2 = 50
                                                                We put the cubes consistently. First, we
                                                                put 40 cubes and there is free space
                                                                left. Then we try to put 11 cubes, but
                                                                there is only space for 10.
                                                                Cubes left: 1 + 7 + 3 + 1 + 5 = 17
print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))
                                There is free space in
                                the box. You could put
                                960 more cubes.

"""


def fill_the_box(height, length, width, *cubes):
    box_vol = height * length * width
    idx = cubes.index('Finish')
    cubes_count = sum(cubes[:idx])
    cubes_space = box_vol - cubes_count
    if box_vol > cubes_count:

        return f"There is free space in the box. You could put {cubes_space} more cubes."
    else:
        return f"No more free space! You have {abs(cubes_space)} more cubes."


#
#
print(fill_the_box(2, 8,
                   2, 2, 1, 7, 3, 1, 5,
                   "Finish"))
print(fill_the_box(5, 5,
                   2, 40, 11, 7, 3, 1, 5,
                   "Finish"))
print(fill_the_box(10, 10,
                   10, 40, "Finish", 2, 15,
                   30))
