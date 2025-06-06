from math import dist
from turtle import *

def turt(cl):
    up()
    m = 10
    tracer(0)
    screensize(1000, 1000)
    for k, col in zip(cl, ['red', 'blue', 'green']):
        for x,y in k:
            goto(x * m, y * m)
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
with open('27_A_21720 (1).txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x,y = map(float, i.split())
        if y > -2:
            k1.append([x, y])
        else:
            k2.append([x, y])

f = center(k1)
s = center(k2)

x = (f[0] + s[0])/2
y = (f[1] + s[1])/2
print(abs(int(x * 10_000)), abs(int(y * 10_000)))

#B
with open('27_B_21720 (1).txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x,y = map(float, i.split())
        if y < -5:
            k1.append([x,y])
        elif y > -5 and x > -6:
            k2.append([x,y])
        else:
            k3.append([x, y])

f = center(k1)
s = center(k2)
t = center(k3)

x = (f[0] + s[0] + t[0])/3
y = (f[1] + s[1] + t[1])/3
print(abs(int(x * 10_000)), abs(int(y * 10_000)))

# turt([k1, k2, k3])

# ans:
# 32540 13646
# 47031 25263