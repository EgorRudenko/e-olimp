import math

n = int(input())

fullCubes = math.floor(pow(n, 1/3))**3
noFullCubes = n - fullCubes

side = pow(fullCubes, 1/3)

width = math.floor(side/2)

if (side % 2) == 0:
    if n == 8:
        print()
    elif noFullCubes == 0:
        print( (2 * ( (side-2) + 1) + 3 * (side - 2)) + (8 * 3) + ( ( ( side - 1 ) ** 2) * ( ( side - 1 ) ** 2 ) ) )

else:
    if n == 1:
        print(12)
    elif noFullCubes == 0:
        print( (2 * ( (side - 2) + 1) + 3 * (side - 2)) + (8 * 3) + ( ( ( side - 1 ) ** 2) *  ( ( side - 1 ) ** 2 ) ) )
    elif noFullCubes < 8:
        pass
