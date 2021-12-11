#First of all I prepared the data as usual

file = open("day5.txt", "r")
text = file.read()
text = text.split("\n")

highestX = 0
highestY = 0
list = []

for i in range(len(text)):
    text[i] = text[i].split(" -> ")

    for j in range(len(text[i])):
         text[i][j] = text[i][j].split(",")

         if int(text[i][j][0]) >= highestX:
             highestX = int(text[i][j][0]) + 1
         if int(text[i][j][1]) > highestY:
             highestY = int(text[i][j][1]) + 1

# end result looks like: [['260', '605'], ['260', '124']]
#                            x1     y1       x2     y2


#make the ocean floor bigger to counter indexexceptions later
if highestX > highestY:
    highestY = highestX
else:
    highestX = highestY


#empty array of full ocean floor size that will get incremented in the future when a line is used
array = []
for i in range(highestY):
    array.append([])
    for j in range(highestX):
        array[i].append(0)



# needed for thinking about how the values are called, helped me developing the algorithm:
#   x1 = text[0][0][0]
#   x2 = text[0][1][0]
#   y1 = text[0][0][1]
#   y2 = text[0][1][1]

#   x1 = text[1][0][0]
#   x2 = text[1][1][0]
#   y1 = text[1][0][1]
#   y2 = text[1][1][1]



#the basic algorithm for horizontal and vertical lines:

for i in range(0, len(text), 1):


    #x coordinates calculation

    if int(text[i][0][0]) > int(text[i][1][0]) and int(text[i][0][1]) == int(text[i][1][1]):
        for j in range(int(text[i][0][0]), int(text[i][1][0]) - 1, -1):
            array[int(text[i][0][1])][j] += 1

    if int(text[i][0][0]) < int(text[i][1][0]) and int(text[i][0][1]) == int(text[i][1][1]):
        for j in range(int(text[i][0][0]), int(text[i][1][0]) + 1, 1):
            array[int(text[i][0][1])][j] += 1
    
    
    #y coordinates calculation
    
    if int(text[i][0][1]) > int(text[i][1][1]) and int(text[i][0][0]) == int(text[i][1][0]):
        for j in range(int(text[i][0][1]), int(text[i][1][1]) - 1, -1):
            array[j][int(text[i][0][0])] += 1

    if int(text[i][0][1]) < int(text[i][1][1]) and int(text[i][0][0]) == int(text[i][1][0]):
        for j in range(int(text[i][0][1]), int(text[i][1][1]) + 1, 1):
            array[j][int(text[i][0][0])] += 1



#count all crossed lines:

counter = 0

for item in array:
    for value in item:
        if int(value) >= 2:
            counter += 1

print("Star 1: ", counter)