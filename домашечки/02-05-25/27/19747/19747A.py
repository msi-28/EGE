from math import dist

with open('27A_19747.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 5:
            k1.append([x, y])
        elif x > 5 and y > 5:
            k2.append([x, y])
        else:
            k3.append([x, y])

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

c1 = center(k1)
c2 = center(k2)
c3 = center(k3)

sx = (c1[0] + c2[0] + c3[0])/3
sy = (c1[1] + c2[1] + c3[1])/3

print(abs(int(sx * 100_000)), abs(int(sy * 100_000)))

