our_list = [34,90,56,43,23,29,87,47]
count = 0
for i in our_list:
    count +=i
# we can do using by sum function that take our_list as an arguement and also do by using count by iterating over for list    
    sumOfour_list = sum(our_list)
    average = count / len(our_list)
print("sum of our list is {}".format(count))    
print("average of ourlist is {}".format(average))     
print(f"sum is {count} and average is {average}")
print("sum function result is {}".format(sumOfour_list))