from math import dist

with open('27_B_17916.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    k5 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 14:
            k1.append([x, y])
        elif 10 < y < 14:
            k2.append([x, y])
        elif 6 < y < 10:
            k3.append([x, y])
        elif 0 < y < 6 and x < 8:
            k4.append([x, y])
        else:
            k5.append([x, y])

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
center4 = center(k4)
center5 = center(k5)

srx = (center1[0] + center2[0] +center3[0] + center4[0] + center5[0])/5
sry = (center1[1] + center2[1] + center3[1] + center4[1] + center5[1])/5

print(int(srx * 10000), int(sry * 10000))