import sys
import re

matrix = []
''' parse input '''
f = open("file2_1.txt")
fileData = f.readlines()
for fileRow in fileData:
    rowInList = re.split("[\t ' ']", fileRow)
    matrix.append(rowInList)

matrix = [[int(x) for x in row] for row in matrix]

totalSum = 0
for row in matrix:
    currMin = sys.maxsize
    currMax = - sys.maxsize - 1
    for elem in row:
        if elem < currMin:
            currMin = elem
        if elem > currMax:
            currMax = elem
    totalSum += currMax - currMin

print(totalSum)
