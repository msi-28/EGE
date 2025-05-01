from math import dist

def centr(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_17882.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x,y = map(float, i.split())
        if x < 1:
            k1.append([x, y])
        else:
            k2.append([x, y])

centr1 = centr(k1)
centr2 = centr(k2)
srx = (centr1[0] + centr2[0])/2
sry = (centr1[1] + centr2[1])/2

print(int(srx * 10_000), int(sry * 10_000))

# ans -> 10738 30730