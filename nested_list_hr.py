# record_list=[]
# if __name__ == '__main__':
#     for n in range(int(input("Enter no of students:"))):
#         name = input("Enter student name:")
#         score = float(input("Enter score:"))
#         tmp_list = [name,score]
#         record_list.append(tmp_list)
# print(record_list)


#print(len(record_list))
# record_list = [['raghu', 1.0], ['harsha', 2.0], ['chidu',3.0]]
# n =(len(record_list))
# print(type(n))
# for i in range(n):
#     print(record_list([i.2]))

# record_list = [['raghu', 2.0], ['harsha', 1.0], ['chidu',8.0]]
# scores= []
# for i in record_list:
    
#     scores.append(i[1])


# print(scores)

# scores= [2,1,8]
# # as=[]
# for i in scores:
#     if i == len(scores):
#         break
#     else:
#         if scores[i] < scores[i+1]:
#             a= scores[i]
#             scores[i]=scores[i+1]
#             scores[i+1]=a
 

# print(scores)


def bubble_sort(arr):
    n = len(arr)
    print(n)

    for i in range(n):
        for j in range(0, n-i-1):
            print(arr)
            print(i,j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

float_list = [3.5, 2.0, 1.1, 4.8, 0.5]

# Call the bubble sort function
bubble_sort(float_list)

# Print the sorted list
print("Sorted list in ascending order:", float_list)



