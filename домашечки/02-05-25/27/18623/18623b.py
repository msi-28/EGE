from math import dist

with open('27B_18623.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 9/8*(x -4):
            k1.append([x, y])
        elif (y > 9/8*(x - 4)) and (y < -(7/5)*(x - 8)):
            k2.append([x, y])
        else:
            k3.append([x, y])

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
c3 = center(k3)

sx = (c1[0] + c2[0] + c3[0])/3
sy = (c1[1] + c2[1] + c3[1])/3

print(int(sx * 100_000),int(sy * 100_000))

# ans -> 398800 348577