from math import *

with open('27A_18623.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 4:
            k1.append([x, y])
        else:
            k2.append([x, y])

def center(k):
    distance = []
    for d in k:
        sum_dist = 0
        for d2 in k:
            sum_dist += dist(d, d2)
        distance.append([sum_dist, d])
    return min(distance)[1]

c1 = center(k1)
c2 = center(k2)

sx = (c1[0] + c2[0])/2
sy = (c1[1] + c2[1])/2

print(int(sx * 100_000),int(sy * 100_000))

# ans -> 398800 348577