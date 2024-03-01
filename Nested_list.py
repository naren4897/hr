my_list=[]
temp_list=[]
n=int(input('Enter the no of sub_lists: '))
for i in range(n):
    for j in range (2):
        temp_list.append(input())
    my_list.append(temp_list)
    temp_list=[]
print(my_list)

