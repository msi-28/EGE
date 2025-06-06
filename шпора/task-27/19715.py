from math import dist
from turtle import *

def turt(cl):
    up()
    m = 1
    tracer(0)
    screensize(1000, 1000)
    for k, col in zip(cl, ['red', 'blue', 'green', 'black']):
        for x,y in k:
            goto(x*m, y*m)
            dot(3, col)
    done()

def center(k):
    distance = []
    for dot1 in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]

#A
with open('27.21.A_19715 (1).txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1
clasters = []
while data:
    claster = [data.pop()]
    for dot1 in claster:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    if len(claster) > 10:
        clasters.append(claster)

c1 = center(clasters[0])
c2 = center(clasters[1])

x = (c1[0] + c2[0])/2
y = (c1[1] + c2[1])/2

print(abs(int(x * 10_000)), abs(int(y * 10_000)))

#B
with open('27.21.B_19715 (1).txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 3
clasters = []
while data:
    claster = [data.pop()]
    for dot1 in claster:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    if len(claster) > 10:
        clasters.append(claster)
centers = [center(c) for c in clasters]
x = sum([c[0] for c in centers])/len(clasters)
y = sum([c[1] for c in centers])/len(clasters)
print(abs(int(x * 10_000)), abs(int(y * 10_000)))
# ans:
# 132035 86733
# 13054 128771