if __name__ == '__main__':
    # Number of students in the class
    n = int(input("Enter the number of students: "))

    # Initialize an empty nested list to store student information
    students = []

    # Input student names and grades
    for _ in range(n):
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        students.append([name, grade])

    # Sort the students based on their grades
    students.sort(key=lambda x: x[1])

    # Find the second lowest grade
    lowest_grade = students[0][1]
    second_lowest_grade = None

    for student in students:
        if student[1] > lowest_grade:
            second_lowest_grade = student[1]
            break

    # Find and print names of students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

    # Sort the names alphabetically
    second_lowest_students.sort()

    # Print the names
    print("Students with the second lowest grade:")
    for name in second_lowest_students:
        print(name)