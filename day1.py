

file = open("adventofcode2021/day1.txt", "r")
depth = file.read().split("\n")



def starOne():
    counter = 1

    for i in range(len(depth) - 1):
        if depth[i] < depth[i+1]:
            counter += 1
    return counter



def starTwo():
    counter = 0
    for i in range(len(depth) - 3):
        if (int(depth[i]) + int(depth[i+1]) + int(depth[i+2])) < (int(depth[i+1]) + int(depth[i+2]) + int(depth[i+3])):
            counter += 1
    return counter

print("Star 1: ", starOne())
print("Star 2: ", starTwo())