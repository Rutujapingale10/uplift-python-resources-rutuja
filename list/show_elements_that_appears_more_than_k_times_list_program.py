ourList = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
result = []
for i in ourList:
    frequency = ourList.count(i)
    if(frequency > k) and i not in result:
        result.append(i)
print(result)