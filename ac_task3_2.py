import sys

def main():
    inputNumber = 368078
    squareSize = 5 # incremented by 2 every four sides
    distToLeftVal = 9 # incremented by 2 after switch to next side of a square; (currentIndex - distToLeftVal) gives an index of a left neighbour
    currentIndex = 9
    nodesNumberTypeC = 0
    memoryList = [1,1,2,4,5,10,11,23,25] # we start with square size 3

    # nodes' types explanation (node of type A is the first one processed in each square):
    # square with size 7:
    # e d c c c b e
    # b           d
    # c           c
    # c           c
    # c           b
    # d           a
    # e b c c c c d
    # change of square's size means incrementing/decrementing number of C type nodes by 2 on each side

    flag = True
    while (flag):
        for i in range(0, 4):
            if i == 0:
                # first side of current square - process a node of type A
                nextValue = getNodeTypeA(memoryList, distToLeftVal, currentIndex, inputNumber)
                currentIndex += 1
                memoryList.append(nextValue)
            # process a node of type B
            nextValue = getNodeTypeB(memoryList, distToLeftVal, currentIndex, inputNumber)
            currentIndex += 1
            memoryList.append(nextValue)
            # process all nodes of type C
            for j in range(0, nodesNumberTypeC):
                nextValue = getNodeTypeC(memoryList, distToLeftVal, currentIndex, inputNumber)
                currentIndex += 1
                memoryList.append(nextValue)
            # process a node of type D
            nextValue = getNodeTypeD(memoryList, distToLeftVal, currentIndex, inputNumber)
            currentIndex += 1
            memoryList.append(nextValue)
            if i < 3:
                # process a node of type E
                nextValue = getNodeTypeE(memoryList, distToLeftVal, currentIndex, inputNumber)
                currentIndex += 1
                memoryList.append(nextValue)

            if i == 0 or i == 2:
                # after first side is processed increment node number of type C by 1
                nodesNumberTypeC += 1
            distToLeftVal += 2
            if nextValue > inputNumber:
                #print(memoryList)
                flag = False
                break

        squareSize += 2

def getNodeTypeA(memoryList, distToLeftNode, idx, inputNumber):
    calculatedValue = memoryList[idx - 1] + memoryList[idx + 1 - distToLeftNode]
    validateCurrentValue(calculatedValue, inputNumber)
    return calculatedValue

def getNodeTypeB(memoryList, distToLeftNode, idx, inputNumber):
    calculatedValue = memoryList[idx - 1] + memoryList[idx - 2] + memoryList[idx - distToLeftNode] + memoryList[idx + 1 - distToLeftNode]
    validateCurrentValue(calculatedValue, inputNumber)
    return calculatedValue

def getNodeTypeC(memoryList, distToLeftNode, idx, inputNumber):
    calculatedValue = memoryList[idx - 1] + memoryList[idx - distToLeftNode - 1] + memoryList[idx - distToLeftNode] + memoryList[idx + 1 - distToLeftNode]
    validateCurrentValue(calculatedValue, inputNumber)
    return calculatedValue

def getNodeTypeD(memoryList, distToLeftNode, idx, inputNumber):
    calculatedValue = memoryList[idx - 1] + memoryList[idx - distToLeftNode - 1] + memoryList[idx - distToLeftNode]
    validateCurrentValue(calculatedValue, inputNumber)
    return calculatedValue

def getNodeTypeE(memoryList, distToLeftNode, idx, inputNumber):
    calculatedValue = memoryList[idx - 1] + memoryList[idx - 1 - distToLeftNode]
    validateCurrentValue(calculatedValue, inputNumber)
    return calculatedValue

def validateCurrentValue(cV, inputNr):
    if cV > inputNr:
        print("THE ANSWER IS: " + str(cV))
        return True
    else:
        return False

if __name__=="__main__":
    main()
