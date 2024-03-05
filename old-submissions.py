# simple helllo word
if __name__ == '__main__':
    print("Hello, World!")

#----------------------------------------------
#if else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
# if n >= 20 and n/2 = 0 && 5>n>2
#     print('Not Weird')
# elif n/2





# if n/2 != 0 or n/2 == 0 & 20>n>6:
#     print('Not Weird')
# else:
#     print('Weird')

# if n % 2 != 0:
#     print('Weird')
# elif n % 2 == 0 and 2 <= n <= 5:
#     print('Not Weird')
# elif n % 2 == 0 and 6 <= n <= 20:
#     print('Weird')
# elif n % 2 == 0 and n > 20:
#     print('Not Weird')
    
    
if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
    print('Weird')
else:
    print('Not Weird')
#----------------------------------------------
#add sum multiply

if __name__ == '__main__':
    a = int(input())
    b = int(input())
# print (a+b)
# print (a-b)
# print (a*b)

print(a + b, a - b, a * b, sep="\n")
#----------------------------------------------
# division and floot division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a//b,f'{a/b:.11f}', sep="\n")

#----------------------------------------------
#loops

if __name__ == '__main__':
    n = int(input())  
for i in range (0,n):
    print (i*i)

#----------------------------------------------
def is_leap(year):
    leap = False
    
    # Write your logic here
    # if year%4==0 and year%100!=0 and year%400==0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    
    return leap

year = int(input())

#----------------------------------------------

#print function

if __name__ == '__main__':
    n = int(input())
# if n <= 150:
#     for n in range (n):
#         print(n+1,end="")
# else:
#     print("Enter no within 150")
    
    
    if n <= 150:
        for i in range(1, n + 1):
            print(i, end="")
    else:
        print("Enter a number within 150.")

#----------------------------------------------
#list Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
coordinates = []

# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 coordinates.append([i, j, k])

# print(coordinates)    
    

coordinates = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

print(coordinates)


#----------------------------------------------

#runner up scores
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
if n <2 or n>10:
    print('no of participents should be in range of 2-10')
else:
    arr = list(arr)
    if len(arr)!=n:
        print(f"you must enter exactly {n} scores.")
    else:
        if all(-100<=score<=100 for score in arr):
            max_score = second_max = float('-inf')
            for score in arr:
                if score > max_score:
                    second_max = max_score
                    max_score = score
                elif score > second_max and score < max_score:
                    second_max = score
            if second_max == float("-inf"):
                print("there is no runner-up score.")
            else:
                print(second_max)
        else:
            print("All scores must be in the range of -100 to 100")


#----------------------------------------------
#second-lowest student
if __name__ == '__main__':
    students = []
    for n in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

students.sort(key=lambda x:x[1])

lowest_grade = students[0][1]
second_lowest_grade = None

for student in students:
    if student[1] > lowest_grade:
        second_lowest_grade = student[1]
        break

second_lowest_students = [student[0] for student in students if student[1]== second_lowest_grade]

second_lowest_students.sort()

for name in second_lowest_students:
    print(name)
#----------------------------------------------

#finding-the-percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
if query_name in student_marks:
    # print (sum(student_marks[query_name]))
    # print (len(student_marks[query_name]))
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    #print(f"The average score for {query_name} is {average_score:.2f}")
    print(f"{average_score:.2f}")
else:
    print(f"{query_name} is not found in the records.")

#----------------------------------------------


#----------------------------------------------



#----------------------------------------------



#----------------------------------------------



#----------------------------------------------



#----------------------------------------------




#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
