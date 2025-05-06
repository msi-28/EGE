from math import dist

with open('27_B_20816.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x,y  = map(float, i.split())
        if x < -5:
            k1.append([x, y])
        elif x > -5 and y < -5:
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

srx = (center1[0] + center2[0] + center3[0])/3
sry = (center1[1] + center2[1] + center3[1])/3

print(abs(int(srx * 10000)), abs(int(sry * 10000)))

# ans -> 15981 37287