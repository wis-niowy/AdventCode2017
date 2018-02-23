import sys

inputNumber = 368078
squareSize = 1
shortestPossibleDistance = 0
countedDistance = 0

#iterate through square's rings until the one containing inputNumber is found
while inputNumber > squareSize**2:
    squareSize += 2
    shortestPossibleDistance += 1

prevSquareSize = squareSize - 2
currentRingLowestValue = prevSquareSize**2 + 1

#check corners first
for j in range(1,4):
    if prevSquareSize**2 + j*(squareSize - 1) == inputNumber:
        countedDistance = 2 * shortestPossibleDistance

for i in range(int(squareSize/2)):
    currentValue = currentRingLowestValue + i
    mirrorReflection = currentValue + (squareSize - 2 - (2*i + 1))
    for j in range(4):
        currentValueShift = j * (squareSize - 1) # shift to another side of a square
        if currentValue + currentValueShift == inputNumber or mirrorReflection + currentValueShift == inputNumber:
            countedDistance = 2 * shortestPossibleDistance - (i + 1)

print(countedDistance)

    