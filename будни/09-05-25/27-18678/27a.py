from math import dist

with open('a.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 2:
            k1.append([x, y])
        elif y > 2 and 1 < x < 6:
            k2.append([x, y])

def center(k):
    distnace = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distnace.append([sum_dist, dot])
    return min(distnace)[1]

c1 = center(k1)
c2 = center(k2)

cx = (c1[0] + c2[0])/2
cy = (c1[1] + c2[1])/2

print(abs(int(cx * 100_000)), abs(int(cy * 100_000)))

# ans -> 346070 215898