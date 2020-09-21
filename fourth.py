import math

a = input()
a = a.split(" ")

x1 = float(a[0])
y1 = float(a[1])
r1 = float(a[2])
x2 = float(a[3])
y2 = float(a[4])
r2 = float(a[5])

distance = round(math.sqrt(((x1-x2)**2)+((y1-y2)**2)), 3)

dis = round(math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) ))
if dis > (r1 + r2):
    print(0)


if r1 > dis:
    if (dis + r2) < r1:
        print(0)
    elif (dis + r2) == r1:
        print(1)
    
    
