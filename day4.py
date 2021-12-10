import re


def ClearUpData():
    file = open("adventofcode2021/day4.txt", "r")
    fields = file.read()
    fields = fields.replace(" ", "\n")
    fields = fields.split("\n")
    for i in range(len(fields) -1, -1, -1):
        if fields[i] == "":
            fields.pop(i)
    
    return fields


def StarOne(numbers, fields):

    index = -1
    winningNumber = 0
    ret = 0

    for i in range(len(numbers)):


        #condition
        if index != -1:
            break
        winningNumber = int(numbers[i])


        #replace drawn numbers with -1
        for j in range(len(fields)):
            if numbers[i] == fields[j]:
                fields[j] = "-1"
            
        
        #check for bingo horizontally
        for k in range(0, len(fields) - 5, 5):
            if fields[k] == "-1" and fields[k+1] == "-1" and fields[k+2] == "-1" and fields[k+3] == "-1" and fields[k+4] == "-1":
                index = k
                break

        #check for bingo vertically
        for k in range(0, len(fields) - 20, 25):
            if fields[k] == "-1" and fields[k+5] == "-1" and fields[k+10] == "-1" and fields[k+15] == "-1" and fields[k+20] == "-1":
                index = k
                break
        for k in range(1, len(fields) - 20, 25):
            if fields[k] == "-1" and fields[k+5] == "-1" and fields[k+10] == "-1" and fields[k+15] == "-1" and fields[k+20] == "-1":
                index = k
                break        
        for k in range(2, len(fields) - 20, 25):
            if fields[k] == "-1" and fields[k+5] == "-1" and fields[k+10] == "-1" and fields[k+15] == "-1" and fields[k+20] == "-1":
                index = k
                break
        for k in range(3, len(fields) - 20, 25):
            if fields[k] == "-1" and fields[k+5] == "-1" and fields[k+10] == "-1" and fields[k+15] == "-1" and fields[k+20] == "-1":
                index = k
                break        
        for k in range(4, len(fields) - 20, 25):
            if fields[k] == "-1" and fields[k+5] == "-1" and fields[k+10] == "-1" and fields[k+15] == "-1" and fields[k+20] == "-1":
                index = k
                break  
         
    #set index to startindex of the winning field
    for i in range (index, 0, -1):
        if i % 25 == 0:
            index = i
            break
    
    #sum up all numbers of that board that are not "-1"
    for i in range(index, index+25):
        if fields[i] != "-1":
            ret += int(fields[i])
    
    return ret * winningNumber   



#Main
        
fields = ClearUpData()
numbers = fields[0].split(",")
fields.pop(0)

print("Star 1:", StarOne(numbers, fields))