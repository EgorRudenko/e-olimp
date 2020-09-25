import math

n = int(input())


def createCube(n):
    matches = 0
    isSolved = False
    noUsed = 0
    s = math.floor(pow(n, 1/3)+0.0001)
    hor = ((2*s) + (2*(s**2))) * (s + 1)
    ver = ((s + 1)**2) * s
    matches = hor + ver
    noUsed = n - (s**3)
    if noUsed == 0:
        isSolved = True
    if s**3 == 1:
        return [0, noUsed+1, False, 0]
    return [matches, noUsed, isSolved, s]

def createSquere(n, s):
    matches = 0
    isSolved = False
    noUsed = 0
    side = math.floor(math.sqrt(n))
    if side > s:
        side -= side - s
    noUsed = n - (side**2)
    matches = ( 2 * side ) + ( 2 * ( side ** 2 )) + (( side + 1 ) ** 2)
    if noUsed == 0:
        isSolved = True
    return [matches, noUsed, isSolved, side]

a = createCube(n)
matches = a[0]
noUsed = a[1]
isSolved = a[2]
identeficator = False
s = a[3]

while isSolved != True:
    pass

'''
while isSolved != True:
    a = createCube(noUsed)
    matches += a[0] - a[3]
    noUsed = a[1]
    if a[0] == 0:
        if noUsed < 4:
            if side1 > 0 and side1 != s or side > 0 and side != s:
                if noUsed == 1:
                    matches += 5
                    noUsed -= 1
                elif noUsed ==2:
        
            matches += 8
                    noUsed -= 2
                if noUsed == 3:
                    if side1 >= 3 and side1 != s or side >= 3:
                        matches += 12
                        noUsed -= 3
                    else:
                        matches += 17
                        noUsed -= 3
            else:
                if noUsed == 1:
                    matches += 8
                    noUsed -= 1
                elif noUsed ==2:
                    matches += 12
                    noUsed -= 2
                elif noUsed ==3:
                    matches += 17
                    noUsed -= 3
        b = createSquere(noUsed, a[3])
        noUsed = b[1]
        matches += b[0]
        isSolved = b[2]
        side = b[3]
        if identeficator == False:
            side1 = side
        identeficator = True
    if noUsed == 0:
        isSolved = True
'''

