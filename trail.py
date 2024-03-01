students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

students.sort(key=lambda x: x[1])

second_lowest_grade =None

for student in students:
    if second_lowest_grade is None or student[1] > second_lowest_grade:
        second_lowest_grade = student[1]
        break
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

second_lowest_students.sort()

print("Students with the second lowest grade:")
for name in second_lowest_students:
    print(name)
