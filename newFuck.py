import math

n = int(input())


def createCube(n):
    isSolved = False
    result = 0
    if n != 0:
        side = math.floor(pow(n,1/3) + 0.0001)  #How long cube edge
        width = math.floor(side / 2)                        #Half of cube edge
        noUsed = n - (side**3)                  #No used cubes
        s = math.floor(side)                    #Side, but more short name
        if side == 1:                           #If cube edge = 1
            if noUsed == 0: 
                result = 12
            else:
                result == noUsed * 8 + 12
            isSolved = True
        elif side == 2:
            if noUsed == 0:
                result = 90
            else:
                while noUsed != 0:
                    a = math.floor(math.sqrt(noUsed))
                    noUsed -= a**2
                    result += ((a-1+1)**2)+((a+1)**2)
                result += 90
            isSolved = True
        elif (side % 2) == 0:
            for i in range(width):
                result += (( (s-(2*i)-1) + 1 )**2) + (( (s-(2*i)-1) + 1 )**2) + (2*((s-(2*i)-2)-1)+3*(s-(2*i)-2)) + (8*3)
            #result = (( (s-1) + 1 )**2) + (( (s-1) + 1 )**2) + (2*((s-2)-1)+3*(s-2)) + (8*3)
        else:
            for i in range(width):
                result += (( (s-(2*i)-1) + 1 )**2) + (( (s-(2*i)-1) + 1 )**2) + (2*((s-(2*i)-2)-1)+3*(s-(2*i)-2)) + (8*3)
            #result = (( (s-1) + 1 )**2) + (( (s-1) + 1 )**2) + (2*((s-2)-1)+3*(s-2)) + (8*3)
            result += 12
    else:
        result = 0
        noUsed =0
        side = 0
        isSolved = True
    return [result, noUsed, side, isSolved]

a = createCube(n)

matches = a[0]
noUsed = a[1]
side = a[2]
isSolved = a[3]
side1 = 0
side1 = math.floor(math.sqrt(noUsed))
#The start of not working shit
'''
if noUsed != 1 and noUsed !=2 and noUsed != 3:
    while isSolved != True:
        if noUsed ==1:
            matches += 4
            noUsed -= 1
        if noUsed == 2:
            matches += 8
            noUsed -= 2
        elif noUsed == 3:
            if side1 <= 2:
                matches += 12
            else:
                matches += 10
            noUsed -= 3
        sideOfOptimalSquere = math.floor(math.sqrt(noUsed))
        if sideOfOptimalSquere > side:
            sideOfOptimalSquere -= (sideOfOptimalSquere - side)
            noUsed += (sideOfOptimalSquere - side) **2
        matches += (((sideOfOptimalSquere-1)+1)**2)+(((sideOfOptimalSquere-1)+1)**2)
        noUsed -= (sideOfOptimalSquere**2)
        if noUsed == 0:
            isSolved = True
else:
    if noUsed == 1:
        matches += 8
        noUsed -= 1
    elif noUsed == 2:
        matches += 12
        noUsed -= 2
    elif noUsed == 3:
        matches += 17
        noUsed -= 3
'''
#The end of not working shit
print(matches)


















