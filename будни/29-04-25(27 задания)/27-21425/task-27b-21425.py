from math import dist

with open('27_B_21425.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x, y = map(float, i.split())
        if x > 20 and y < 0:
            k1.append([x,y])
        elif 2 < x < 30 and y > 10:
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

center1 = center(k1)
center2 = center(k2)
center3 = center(k3)

ansx = (center1[0] + center2[0] + center3[0])/3
ansy = (center1[1] + center2[1] + center3[1])/3

print(int(ansx * 10_000), int(ansy * 10_000))

# ans -> 122627 29105