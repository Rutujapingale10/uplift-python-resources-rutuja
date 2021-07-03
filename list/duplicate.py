ourList = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


def repeatedElements(x):
    size = len(x)
    repeatedElementsInList = []
    for i in range(size):
        for j in range(i+1, size):
            if x[i] == x[j] and x[i] not in repeatedElementsInList:
                repeatedElementsInList.append(x[i])
    return repeatedElementsInList


print(repeatedElements(ourList))