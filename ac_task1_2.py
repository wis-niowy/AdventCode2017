f = open("file1_1.txt")
data = f.readline()
input = data
inputLength = len(input)
stepForward = int(int(inputLength) / 2)
totalSum = 0

for i in range(0, inputLength):
    if input[i] == input[(i+stepForward)%inputLength]:
        totalSum += int(input[i])

print(totalSum)
