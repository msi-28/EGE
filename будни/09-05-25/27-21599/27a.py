from math import dist
# from turtle import *
#
# m = 10
# tracer(0)
# screensize(1000, 1000)

with open('a.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -6:
            k3.append([x, y])
        elif (y > -6) and (y < x - 12):
            k2.append([x, y])
        else:
            k1.append([x, y])

# up()
# for k, col in zip([k1, k2, k3], ['red', 'blue', 'green']):
#     for x, y in k:
#         goto(x * m, y * m)
#         dot(3, col)
#
# done()

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
c3 = center(k3)

cx = (c1[0] + c2[0] + c3[0])/3
cy = (c1[1] + c2[1] + c3[1])/3

print(abs(int(cx * 10_000)), abs(int(cy * 10_000)))

# ans -> 178755 2896