import sys
import re

matrix = []
#parse input
f = open("file2_1.txt")
fileData = f.readlines()
for fileRow in fileData:
    rowInList = re.split("[\t ' ']", fileRow)
    matrix.append(rowInList)

matrix = [[int(x) for x in row] for row in matrix]

totalSum = 0
for row in matrix:
    for i in range(len(row)):
        for j in range(len(row)):
            if i != j and row[i] % row[j] == 0:
                totalSum += int(row[i] / row[j])


print(totalSum)

