from math import dist

with open('27_B_21720.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1.4
clasters = []

while data:
    claster = [data.pop()]
    for dot in claster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    clasters.append(claster)

# print([len(k) for k in clasters])

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

centerx = [center(k)[0] for k in clasters]
centery = [center(k)[1] for k in clasters]

srx = sum(centerx)/len(clasters)
sry = sum(centery)/len(clasters)

print(abs(int(srx * 10000)), abs(int(sry * 10000)))

# ans -> 47031 25263