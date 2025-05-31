from math import dist

with open('27.13.B_19567.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.7
clasters = []
while data:
    claster = [data.pop()]
    for dot in claster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    clasters.append(claster)
print(len(clasters))

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot2, dot)
        distance.append([sum_dist, dot])
    return min(distance)[1]

csx = [center(claster)[0] for claster in clasters]
csy = [center(claster)[1] for claster in clasters]

sx = sum(csx)/len(clasters)
sy = sum(csy)/len(clasters)

print(int(sx * 10_000), abs(int(sy * 10_000)))

# 3785 46909