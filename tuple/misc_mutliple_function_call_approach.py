"""
Lets' say we have four tuples and we have four list
Now, we need to write a program where we can have all those elements but in an alterate manner
but the twist is the user would choose the first set of elements

[1,2] [3,4] [5,6] [7, 8, 9]
(11,12) (13,14) (15,16) (17, 18, 19)

1 for list and 2 for tuple 
so, if the user says that i want 1 
then the entry will be 1 2 11 12 3 4 13 14 5 6 15 16 7 8 9 17 18 19
then the entry will be 1 2 11 12 3 4 13 14 5 6 15 16 7 8 9 17 18 19
"""

result_list = []

list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
list4 = [7, 8, 9]

tuple1 = (11, 12)
tuple2 = (13, 14)
tuple3 = (15, 16)
tuple4 = (17, 18, 19)


list5 = list(tuple1)
list6 = list(tuple2)
list7 = list(tuple3)
list8 = list(tuple4)



def add_list(mylist1):
    for i in range(len(mylist1)):
        result_list.append(mylist1[i])

    return result_list


user_inp = int(input("Enter 1 or 2: (1 for list, 2 for tuple)"))

if user_inp == 1:
    add_list(list1)
    add_list(list5)
    add_list(list2)
    add_list(list6)
    add_list(list3)
    add_list(list7)
    add_list(list4)
    add_list(list8)

elif user_inp == 2:
    add_list(list5)
    add_list(list1)
    add_list(list6)
    add_list(list2)
    add_list(list7)
    add_list(list3)
    add_list(list8)
    add_list(list4)

else:
    print("Sorry, Wrong Input")
    exit()

print(result_list)