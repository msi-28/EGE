from math import dist

def center(k):
    distance = []
    for dot1 in k:
        sum_dist = 0
        for dot2 in k:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]
#A
with open('27_A_19257.txt') as file:
    k1 = []
    k2 = []
    for i in file:
        x,y = map(float, i.split())
        if y > 8:
            k1.append([x,y])
        else:
            k2.append([x,y])

c1 = center(k1)
c2 = center(k2)

x = (c1[0] + c2[0])/2
y = (c1[1] + c2[1])/2
print(abs(int(x * 10_000)), abs(int(y * 10_000)))

#B
with open('27_B_19257.txt') as file:
    k1 = []
    k2 = []
    k3 = []
    for i in file:
        x,y = map(float, i.split())
        if y > 8:
            k1.append([x,y])
        elif y < 8 and x > 0:
            k2.append([x,y])
        else:
            k3.append([x,y])

c1 = center(k1)
c2 = center(k2)
c3 = center(k3)

x = (c1[0] + c2[0] + c3[0])/3
y = (c1[1] + c2[1] + c3[1])/3
print(abs(int(x * 10_000)), abs(int(y * 10_000)))

# ans:
# 43789 62202
# 14271 54727