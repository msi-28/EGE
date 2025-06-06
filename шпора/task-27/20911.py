from math import dist
from turtle import *

#A
# with open('27_A_20911.txt') as file:
#     k1 = []
#     k2 = []
#     for i in file:
#         x,y = map(float, i.split())
#         if y > 0:
#             k1.append([x,y])
#         else:
#             k2.append([x,y])
#
def center(k):
    distance = []
    for dot in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]
#
# f = center(k1)
# s = center(k2)
#
# x = (f[0] + s[0])/2
# y = (f[1] + s[1])/2

# print(abs(int(x*10_000)), abs(int(y*10_000)))

# 28603 10294

#B
with open('27_B_20911.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clasters = []
eps = 1
while data:
    claster = [data.pop()]
    for dot1 in claster:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                claster.append(dot2)
                data.remove(dot2)
    clasters.append(claster)

# tracer(0)
# m = 20
# up()
# screensize(1000, 1000)
k1 = clasters[0]
k2 = clasters[1]
k3 = clasters[3]

# for k, col in zip(clasters, ['red', 'blue', 'green']):
#     for x,y in k:
#         goto(x * m,y*m)
#         dot(3,col)

done()

f = center(k1)
s = center(k2)
t = center(k3)

x = (f[0] + s[0] + t[0])/3
y = (f[1] + s[1] + t[1])/3

print(abs(int(x*10_000)), abs(int(y*10_000)))

# 64004 17707