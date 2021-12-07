import re

file = open("day2.txt", "r")
course = file.read().split("\n")



def starOne():
    positionX = 0
    positionY = 0

    for value in course:
        
        cutted = re.split(" ", value)
        
        if cutted[0] == "forward":
            positionX += int(cutted[1])
        elif cutted[0] == "down":
            positionY += int(cutted[1])
        elif cutted[0] == "up":
            positionY -= int(cutted[1])
    return positionX * positionY



def starTwo():
    positionX = 0
    positionY = 0
    aim = 0

    for value in course:
        
        cutted = re.split(" ", value)
        
        if cutted[0] == "forward":
            positionX += int(cutted[1])
            if aim != 0:
                positionY += aim * int(cutted[1])

        elif cutted[0] == "down":
            aim += int(cutted[1])
        elif cutted[0] == "up":
            aim -= int(cutted[1])

    return positionX * positionY


print(starOne())
print(starTwo())