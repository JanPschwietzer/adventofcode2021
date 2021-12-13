file = open("day6.txt")


def Calculation(days):

    array = file.read().split(",")

    for i in range(len(array)):
        array[i] = int(array[i])

    for j in range(days):
        for i in range(len(array)):

            if array[i] >= 1:
                array[i] -= 1
            elif array[i] == 0:
                array.append(8)
                array[i] = 6
        print("Day: ", j)

    return len(array)

print(Calculation(80))