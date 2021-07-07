x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[12, 7, 3], [9, 5, 6], [7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Iterating through the rows
for i in range(len(x)):
    # Iterate through the column
    for j in range(len(x[0])):
        # let's calculate the result matrix's addition
        result[i][j] = x[i][j] + y[i][j]

print(result)