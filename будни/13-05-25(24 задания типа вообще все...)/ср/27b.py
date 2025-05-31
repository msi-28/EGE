from math import dist
# from turtle import *
#
# tracer(0)
# m = 50
# screensize(1000, 1000)

with open('27B_18056.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.8
clasters = []
while data:
    claster = [data.pop()]
    for d in claster:
        for d2 in data.copy():
            if dist(d, d2) < eps:
                claster.append(d2)
                data.remove(d2)
    if len(claster) > 6:
        clasters.append(claster)
print(len(clasters))

# up()
# for k, col in zip(clasters, ['red', 'blue', 'green']):
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

# centers =


# print(abs(int(sx * 100_000)), abs(int(sy * 100_000)))

# ans -> 43744 47901