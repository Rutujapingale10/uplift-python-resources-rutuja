test_list = [55,4,6.0,True,8.0,"fghh",False,"fgrg","erqert"]
print(f"my test list is {test_list}")

result1 = len(list(i  for i in test_list if isinstance(i,int) and not isinstance(i,bool)))
result2 = len(list(i  for i in test_list if isinstance(i,str)))
result3 = len(list(i  for i in test_list if isinstance(i,float)))
result4 = len(list(i  for i in test_list if isinstance(i,bool)))




print("count of integer is{}".format(result1))
print("count of str is{}".format(result2))
print("count of float is{}".format(result3))
print("count of bool is{}".format(result4))