list = []
for i in range(0,9):
    list.append(int(input()))
print(list)    

#list = [30,50,33,4,45,32,90,67,39,9.5]
even_list = []
odd_list = []
for i in range(len(list)):
    if(list[i] % 2 == 0):
        even_list.append(list[i])
    else:
        odd_list.append(list[i])
print(f"my even list is {even_list}")  
print(f"my odd list is {odd_list}")       
print(f"element present in even list = {len(even_list)} and elements present in odd list = {len(odd_list)}")   