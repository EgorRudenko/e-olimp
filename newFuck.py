import math

n = input()


def createCube(n):
    if n != 0:
        side = math.floor(pow(n,1/3) + 0.0001)  #How long cube edge
        width = side / 2                        #Half of cube edge
        noUsed = n - (side**3)                  #No used cubes
        s = math.floor(side)                    #Side, but more short name
        if side == 1:                           #If cube edge = 1
            if noUsed == 0: 
                result = 12
            else:
                result == noUsed * 8 + 12
        elif side == 2:
            pass
        elif (width % 2) == 0:
            #result = (( (s-1) + 1 )**2) + (( (s-1) + 1 )**2) + (2*((s-2)-1)+3*(s-2)) + (8*3)
        else:
            #result = (( (s-1) + 1 )**2) + (( (s-1) + 1 )**2) + (2*((s-2)-1)+3*(s-2)) + (8*3)
        return [result, noUsed]
