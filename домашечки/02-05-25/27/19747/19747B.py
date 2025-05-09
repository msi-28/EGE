from math import dist
from turtle import *
tracer(0)
m = 40
screensize(2000, 2000)

with open('27B_19747.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    k5 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 10 and y < x:
            k1.append([x, y])
        elif x < 10 and y > x   :
            k2.append([x, y])
        elif x > 10 and y > x:
            k3.append([x, y])
        elif x > 10 and y < x and y > 10:
            k4.append([x, y])
        else:
            k5.append([x, y])

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

up()
for k, col in [[k1, 'red'], [k2, 'blue'], [k3, 'green'], [k4, 'orange'], [k5, 'black']]:
        k = sorted(k, key=lambda x: x[1])
        print(k)
        for x, y in k:
            goto(x * m, y * m)
            dot(3, col)

done()


c1 = center(k1)
c2 = center(k2)
c3 = center(k3)
c4 = center(k4)
c5 = center(k5)

sx = (c1[0] + c2[0] + c3[0] + c4[0] + c5[0])/5
sy = (c1[1] + c2[1] + c3[1] + c4[1] + c5[1])/5

print(abs(int(sx * 100_000)), abs(int(sy * 100_000)))

# ans -> 1091104 954833