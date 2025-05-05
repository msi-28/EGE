from math import dist

with open('27_A_21911.txt') as file:
     data = [list(map(float, i.split())) for i in file]

eps = 2
ks = []
while data:
    k = [data.pop()]
    for dot in k:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                k.append(dot2)
                data.remove(dot2)
    ks.append(k)

def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot1 in k:
            sum_dist += dist(dot, dot1)
        distance.append([sum_dist, dot])
    return min(distance)[1]

centerx = [center(k)[0] for k in ks]
centery = [center(k)[1] for k in ks]

srx = sum(centerx)/len(ks)
sry = sum(centery)/len(ks)

print(int(srx * 10000), int(sry * 10000))

# ans -> 26216 24182