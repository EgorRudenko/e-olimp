import math

n = int(input())

fullCubes = math.floor(pow(n, 1/3))**3
noFullCubes = n - fullCubes

side = pow(fullCubes, 1/3)

width = math.floor(side/2)

if (side % 2) == 0:
    pass
else:
    if n == 1:
        print(12)
    elif noFullCubes == 0:
        print()
