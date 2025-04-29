from math import dist

def centr(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_B_17882.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x,y = map(float, i.split())
        if x > 5:
            k1.append([x, y])
        elif 2<x<5 and y > 6:
            k2.append([x, y])
        else:
            k3.append([x, y])

centr1 = centr(k1)
centr2 = centr(k2)
centr3 = centr(k3)
srx = (centr1[0] + centr2[0] + centr3[0])/3
sry = (centr1[1] + centr2[1] + centr3[0])/3

print(int(srx * 10_000), int(sry * 10_000))

# ans - > 37522 51328