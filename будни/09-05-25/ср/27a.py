from math import dist

from h5py.h5pl import append

with open('27.13.A_19567.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 0: k1.append([x, y])
        else: k2.append([x, y])

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot2, dot)
        distance.append([sum_dist, dot])
    return min(distance)[1]

c1 = center(k1)
c2 = center(k2)

print(c1, c2)
sx = (c1[0] + c2[0])/2
sy = (c1[1] + c2[1])/2

print(int(sx * 10_000), abs(int(sy * 10_000)))