import copy

file = open("day3.txt", "r")
input = file.read().split("\n")


def starOne():
    counter1 = 0
    counter0 = 0

    gamma = ""
    epsilon = ""

    for i in range(len(input[0])):

        for value in input:
            if value[i] == "1":
                counter1 += 1
            elif value[i] == "0":
                counter0 += 1

        if counter1 > counter0:
            gamma += "1"
            epsilon += "0"
        elif counter0 > counter1:
            gamma += "0"
            epsilon += "1"
        
        counter1 = 0
        counter0 = 0
    
    return int(gamma, 2) * int(epsilon, 2)



def starTwo():
    gamma = 0
    epsilon = 0
    lenBinNum = 12

    gammaArray = copy.copy(input)
    epsilonArray = copy.copy(input)
    
    counterOne = 0


    for i in range(lenBinNum):
        counterOne = 0

        for j in range(len(gammaArray)):
            if gammaArray[j][i] == "1":
                counterOne += 1
        if counterOne >= len(gammaArray) / 2:
            isOne = "1"
        else:
            isOne = "0"

        for k in range(len(gammaArray) - 1, -1, -1):
            if gammaArray[k][i] != isOne and len(gammaArray) != 1:
                gammaArray.pop(k)

    gamma = gammaArray[0]
    

    for i in range(lenBinNum):
        counterOne = 0

        for j in range(len(epsilonArray)):
            if epsilonArray[j][i] == "1":
                counterOne += 1

        if counterOne >= len(epsilonArray) / 2:
            isOne = "1"
        else:
            isOne = "0"

        for k in range(len(epsilonArray) - 1, -1, -1):
            if epsilonArray[k][i] == isOne and len(epsilonArray) != 1:
                epsilonArray.pop(k)
    
    epsilon = epsilonArray[0]

    return int(gamma, 2) * int(epsilon, 2)
    
    



print("Star 1: ", starOne())
print("Star 2: ", starTwo())