"""
****interchanging first and last element****
input - [45,67,87,90,78]
output - [78,67,87,90,45]
first approach is find the length of element and then swap two element 
how to do this
just take any temparory varible and store value in it and then perform swap operation
"""
def intfirstlast(myList):
    SizeOfmyList = len(myList)
    temp_var = myList[0]
    myList[0] = myList[SizeOfmyList-1]
    myList[SizeOfmyList-1] = temp_var
    return myList


def secondApproach(myList1):
    SizeOfmyList = len(myList1)
    temp_var = myList1[0]
    myList1[0] = myList1[-1]
    myList1[-1] = temp_var
    return myList1

def thirdXYApproach(mylist2):
    mylist2[0],mylist2[-1] = mylist2[-1],mylist2[0]
    return mylist2

# Tupple Approach
def TuppleApproach(mylist3):
    a,*b,c = mylist3
    mylist3 = [c,*b,a]
    return mylist3

#main code driver
new_list = [45,67,87,90,78]
print(intfirstlast(new_list))
new_list1 = [77.8,67,87,90,98]
print(secondApproach(new_list1))
new_list2 = [6.7,89,39,20,100]
print(thirdXYApproach(new_list2))
new_list3 = [89,59,49,39,29,19]
print(TuppleApproach(new_list3))