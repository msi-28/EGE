from math import dist

with open('27A_18056.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x,y = map(float, i.split())
        if y > -1 and x < 1:
            k1.append([x, y])
        elif y < - 1 and x > 1/2:
            k2.append([x, y])
        else:
            continue

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

sx = (c1[0] + c2[0])/2
sy = (c1[1] + c2[1])/2

print(abs(int(sx * 100_000)), abs(int(sy * 100_000)))

# ans -> 43744 47901