from math import dist
import turtle

# m = 5
# turtle.tracer(0)
# turtle.screensize(1000, 1000)

with open('27.19.B_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 3
clasters = []
while data:
    claster = [data.pop()]
    for dot in claster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    if len(claster) > 20:
        clasters.append(claster)

# turtle.up()
# for k, col in zip(clasters, ['red', 'green', 'blue', 'black', 'pink']):
#     for x, y in k:
#         turtle.goto(x * m, y * m)
#         turtle.dot(3, col)
#
# turtle.done()

def center(k):
    distanve = []
    for d in k:
        sum_dist = 0
        for d2 in k:
            sum_dist += dist(d, d2)
        distanve.append([sum_dist, d])
    return max(distanve)[1]

ends = [center(claster) for claster in clasters]
cx = sum([end[0] for end in ends])/len(clasters)
cy = sum([end[1] for end in ends])/len(clasters)

print(int(cx * 10_000), int(cy * 10_000))

# ans -> -209434 474989