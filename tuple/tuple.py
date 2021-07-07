"""find maximum and minimum k elements in tuple


tuple is immutable  
so we cant modify tuple element like list
but there is big chance we can cast it into list and then solve it 
but it is always better we can solve directly it staying in tuple
input = [3,2,7,18,9] k = 2
output= [1,3,9,18]

"""

total_entry = int(input("enter how many element you want in tuple"))
k = int(input("enter the value of k:"))
ourList = []
for i in range(total_entry):
    ourList.append(int(input(f"Enter the {i+1}th Entry: ")))
ourList.sort()
newList = ourList[:k]+ourList[-k:]
# for i in range(k):
#     newList.append(ourList[i])
#     newList.append(ourList[-1-i])
newList.sort()
ourTuple = tuple(newList)
print(ourTuple)