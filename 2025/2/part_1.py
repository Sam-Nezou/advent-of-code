# Adevent of code 2025 Day 2
from input import input_test
from input import input


print(input.index(','))

def convertInputInTable(input):
    inputTable = []

    i = 0
    str = ""
    for i in range(len(input)):
        char = input[i]
        print(char)
        if char == ",":
            inputTable.append(str)
            str = ""
        else:
            str += char

    inputTable.append(str)
    print(inputTable)
    return inputTable

def addingInvalids(invalidsIds):
    res = 0
    for id in invalidIds:
        res += id    
    
    return res

invalidIds = []



for val in convertInputInTable(input):
    indexMiddle = val.index('-')
    startVal = int(val[:indexMiddle])
    endVal = int(val[indexMiddle+1:])
    
    currentVal = startVal

    while currentVal <= endVal:
        strCurrentVal = str(currentVal)
        size = len(strCurrentVal)
        middle = int(size/2)
        left = strCurrentVal[:middle]
        right = strCurrentVal[middle:]
        
        if left == right:
            # print(currentVal)
            # print(left + ':' + right)
            invalidIds.append(currentVal)
        currentVal += 1

print(addingInvalids(invalidIds))

