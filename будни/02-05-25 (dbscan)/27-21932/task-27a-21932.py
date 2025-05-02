from math import dist

with open('27_A_21932.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.9
clasters = []
while data:
    claster = [data.pop()]
    for dot in claster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    clasters.append(claster)

print([len(k) for k in clasters])

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

center1 = center(clasters[0])
center2 = center(clasters[1])

srx = (center1[0])/2
sry = (center1[1] + center2[1])/2

print(int(srx * 10_000), int(sry * 10_000))
