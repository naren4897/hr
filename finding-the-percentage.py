# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for i in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
student_marks={'ram': [20.0, 30.0, 40.0], 'haraha': [40.0, 50.0, 60.0]}
query_name = input()
if query_name in student_marks:
    # print (sum(student_marks[query_name]))
    # print (len(student_marks[query_name]))
    #print (student_marks)
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    #print(f"The average score for {query_name} is {average_score:.2f}")
    print(f"{average_score:.2f}")
else:
    print(f"{query_name} is not found in the records.")
