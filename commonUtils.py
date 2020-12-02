def getInputData():
    f = open("inputData.txt", "r")
    numbers = []
    for line in f:
        numbers.append(int(line))
    return numbers
