"""
You are planning to study at Software University.
You need to choose classes so that you gather enough credits to graduate successfully.
Write a function called gather_credits that receives information about credits needed, courses, and their
credits, and returns the result. The function will receive a different number of arguments. The arguments will be
passed as follows:
 The first argument will be the number of credits you need ‐ an integer in the range [0, 200];
 The following arguments will be the tuples with two elements ‐ the first one is the course name (string),
and the second one is the course credits (integer);
After receiving the information and calling the function, the program should start tracking the enrollment process:
 Take the course’s name from each tuple successively and if you need more credits, enroll in it, and proceed
to the next one.
 If a course has already been enrolled in, ignore it, and proceed to the next one.
 If you have reached the needed number of credits, STOP enrolling!
In the end:
 If you’ve managed to gather the needed credits, return the message, including the enrolled courses on a
new line:
"Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {course1, course2, …, courseN}"
o return the courses’ names sorted alphabetically, in ascending order.
 Otherwise, return the message:
"You need to enroll in more courses! You have to gather {credits_shortage}
credits more."
Note: Submit only the function in the judge system
Constraints
 The first argument will always be an integer.
 Each tuple given will always contain the course name with its credits.

print(gather_credits(
80,
("Basics", 27),
))
                        You need to enroll in more courses! You have to
                        gather 53 credits more.
print(gather_credits(
80,
("Advanced", 30),
("Basics", 27),
("Fundamentals", 27),
))
                        Enrollment finished! Maximum credits: 84.
                        Courses: Advanced, Basics, Fundamentals
print(gather_credits(
60,
("Basics", 27),
("Fundamentals", 27),
("Advanced", 30),
("Web", 30)
))
                        Enrollment finished! Maximum credits: 84.
                        Courses: Advanced, Basics, Fundamentals
"""


def gather_credits(credits_required, *args):
    courses_enrolled = set()
    credits_gathered = 0
    for course, credit in args:
        if course in courses_enrolled:
            continue

        if credits_gathered < credits_required:
            courses_enrolled.add(course)
            credits_gathered += credit
        else:
            break

    if credits_gathered >= credits_required:
        return (f"Enrollment finished! Maximum credits: {credits_gathered}.\n"
                + f"Courses: {', '.join(sorted(courses_enrolled))}")
    else:
        return (f"You need to enroll in more courses! "
                f"You have to gather {credits_required - credits_gathered} credits more.\n")


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))

# print(gather_credits(
# 80,
# ("Basics", 27),
# ))