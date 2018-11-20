numberList = [2, 2, 3, 3, 4, 4, 5, 5]
newList = []

for i in numberList:
    if i not in newList:
        newList.append(i)

print(newList)