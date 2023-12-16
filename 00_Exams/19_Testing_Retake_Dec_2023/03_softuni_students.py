def softuni_students(*args, **kwargs):
    course_student_relation = {}
    invalid_students = []

    for course_id, student in args:

        if course_id not in kwargs:
            invalid_students.append(student)
            continue

        course_student_relation[student] = course_id

    text = []
    for student, course in sorted(course_student_relation.items()):
        text.append(f"*** A student with the username {student} has successfully finished the course {kwargs[course]}!")

    if invalid_students:
        text.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    return '\n'.join(text)


if __name__ == '__main__':
    print(softuni_students(
        ('id_1', 'Kaloyan9905'),
        id_1='Python Web Framework',
    ))
    print('*' * 20)
    print(softuni_students(
        ('id_7', 'Silvester1'),
        ('id_32', 'Katq21'),
        ('id_7', 'The programmer'),
        id_76='Spring Fundamentals',
        id_7='Spring Advanced',
    ))
    print('*' * 20)
    print(softuni_students(
        ('id_22', 'Programmingkitten'),
        ('id_11', 'MitkoTheDark'),
        ('id_321', 'Bobosa253'),
        ('id_08', 'KrasimirAtanasov'),
        ('id_32', 'DaniBG'),
        id_321='HTML & CSS',
        id_22='Machine Learning',
        id_08='JS Advanced',
    ))
    print('*' * 20)
