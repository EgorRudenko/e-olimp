import math

n = int(input())

fullCubes = math.floor(pow(n, 1/3)+0.01)**3
if fullCubes == 1:
    fullCubes = 0
noFullCubes = n - fullCubes

side = math.ceil(pow(fullCubes, 1/3))

width = math.floor(side/2)

s = side
result = 0

print(noFullCubes)


if (side % 2) == 0:
    if n == 8:
        print(36)
    elif noFullCubes == 0:
        result = 0
        for i in range( width ):
            s = s - (2 * i)
            result += (2 * ( (s - 2) + 1) + 3 * (s - 2)) + (8 * 3) + ( ( ( s - 1 ) ** 2) *  ( ( s - 1 ) ** 2 ) )
        print(result)
    elif noFullCubes < 8 and fullCubes != 0:
        if a > 1:
            b = noFullCubes - (a**2)
            for i in range( width ):
                s = s - (2 * i)
                result += (2 * ( (s - 2) + 1) + 3 * (s - 2)) + (8 * 3) + ( ( ( s - 1 ) ** 2) *  ( ( s - 1 ) ** 2 ) ) 
                result += 12
            result += ((a + 1)**2) + ((a + 1)**2)
            if b == 1:
                result += 8
            elif b == 2:
                result += 14
            elif b == 3:
                result += 18
        elif a == 1:
            if noFullCubes == 1:
                result += 8
            elif noFullCubes == 2:
                result += 14
            elif noFullCubes == 3:           
                result += 18

else:
    if n == 1:
        print(12)
    elif noFullCubes == 0:
        result = 0
        for i in range( width ):
            s = s - (2 * i)
            result += (2 * ( (s - 2) + 1) + 3 * (s - 2)) + (8 * 3) + ( ( ( s - 1 ) ** 2) *  ( ( s - 1 ) ** 2 ) )
        result += 12
        print(result)
    elif noFullCubes < 8 and fullCubes != 0:
        a = math.floor(math.sqrt(noFullCubes) + 0.00001)
        if a > 1:
            b = noFullCubes - (a**2)
            for i in range( width ):
                s = s - (2 * i)
                result += (2 * ( (s - 2) + 1) + 3 * (s - 2)) + (8 * 3) + ( ( ( s - 1 ) ** 2) *  ( ( s - 1 ) ** 2 ) )
                result += 12
            result += ((a + 1)**2) + ((a + 1)**2)
            if b == 1:
                result += 8
            elif b == 2:
                result += 14
            elif b == 3:
                result += 18
        elif a == 1:
            if noFullCubes == 1:
                result += 8
            elif noFullCubes == 2:
                result += 14
            elif noFullCubes == 3:
                result += 18
    elif noFullCubes > 8:
        if noFullCubes == 8:
            print(24)
        else:
            while noFullCubes > 0:
                c = math.floor(pow(noFullCubes, 1/3))
                if c > 1:
                    pass
                else:
                    pass
    
    




print(result)




























 
