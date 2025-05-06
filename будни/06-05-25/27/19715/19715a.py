from math import dist
# from turtle import *
#
# m = 10
# tracer(0)
# screensize(1000, 1000)

with open('27.21.A_19715.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 2
clasters = []
while data:
    claster = [data.pop()]
    for d in claster:
        for d2 in data.copy():
            if dist(d, d2) < eps:
                claster.append(d2)
                data.remove(d2)
    if len(claster) > 20:
        clasters.append(claster)

# up()
# for k, col in zip(clasters, ['red', 'blue']):
#     for x, y in k:
#         goto(x * m, y * m)
#         dot(3, col)
# done()

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

centers = [center(claster) for claster in clasters]

sx = sum([c[0] for c in centers])/len(clasters)
sy = sum([c[1] for c in centers])/len(clasters)

print(int(sx * 10_000), int(sy * 10_000))

# ans -> 132035 86733