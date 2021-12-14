file = open("day7.txt", "r")

array = file.read().split(",")


highestValue = 0

for value in array:
    if highestValue < int(value):
        highestValue = int(value)

def StarOne(array):

    fuel = 0
    lowestFuel = 0

    for i in range(highestValue):

        fuel = 0
        
        for j in range(len(array)):
            if i < int(array[j]):
                fuel += int(array[j]) - i
            elif i > int(array[j]):
                fuel +=  i - int(array[j])

        if lowestFuel != 0 and lowestFuel > fuel:
            lowestFuel = fuel
        elif lowestFuel == 0:
            lowestFuel = fuel
    
    return lowestFuel


def StarTwo(array):

    fuel = 0
    lowestFuel = 0


    for i in range(highestValue):
        fuel = 0
        
        for j in range(len(array)):
            counter = 1

            if i < int(array[j]):
                for k in range(int(array[j]), i, -1):
                    fuel += counter
                    counter += 1

            elif i > int(array[j]):
                for k in range(int(array[j]), i, 1):
                    fuel += counter
                    counter += 1

        if lowestFuel != 0 and lowestFuel > fuel:
            lowestFuel = fuel
        elif lowestFuel == 0:
            lowestFuel = fuel
    
    return lowestFuel

print("Star 1: ", StarOne(array))
print("Star 2 takes a moment, please wait..")
print("Star 2: ", StarTwo(array))

    
