import re

file = open("day3.txt", "r")
input = file.read().split("\n")


def starOne(star):
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
    
    if star == "values":
        return gamma, epsilon
    elif star == "answer":
        return int(gamma, 2) * int(epsilon, 2)



#
# STAR 2 NOT WORKING
#

def starTwo():
    gammaEpsi = starOne("values")

    g = gammaEpsi[0]
    e = gammaEpsi[1]

    g = "\A" + g
    e = "\A" + e

    gamma = 0
    epsilon = 0

    for i in range(len(g) - 2):

        for value in input:

            x = re.findall(g, value)
            y = re.findall(e, value)

            if len(x) == 1:
                gamma = value
            if len(y) == 1:
                epsilon = value

        g = g[:-1]
        e = e[:-1]


    return int(gamma, 2) * int(epsilon, 2)
    



print("Star 1: ", starOne("answer"))
# print(starTwo())


        
