f = open("file1_1.txt")
data = f.readline()
input = data
inputLength = len(input)
totalSum = 0

for i in range(0, inputLength):
    if input[i] == input[(i+1)%inputLength]:
        totalSum += int(input[i])

print(totalSum)
