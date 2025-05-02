from math import dist

with open('27_A_21425 (1).txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x,y  = map(float, i.split())
        if y > 0:
            k1.append([x, y])
        else:
            k2.append([x, y])

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

center1 = center(k1)
center2 = center(k2)

srx = (center1[0] + center2[0])/2
sry = (center1[1] + center2[1])/2

print(int(srx * 10000), int(sry * 10000))

# ans -> 167990 73043