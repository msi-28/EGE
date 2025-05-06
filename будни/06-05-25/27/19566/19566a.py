from math import *
from turtle import *

m = 40
tracer(0)
screensize(2000, 1000)

with open('27.17.A_19566.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 5 and y < x - 2 and y < -x:
            k1.append([x, y])
        elif x > 5 and y < -(x - 11):
            k2.append([x, y])

def center(k):
    dists = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return max(dists)[1]

c1 = center(k1)
c2 = center(k2)

up()
for k, col in zip([k1, k2], ['red', 'blue']):
    for x, y in k:
        goto(x * m, y * m)
        dot(3, col)
done()

sx = (c1[0] +  c2[0])/2
sy = (c1[1] +  c2[1])/2

print(int(sx * 10_000), int(sy * 10_000))

