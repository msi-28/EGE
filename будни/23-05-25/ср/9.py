from itertools import *
with open('9_6897.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f(ls):
    for a1, a2, a3, a4 in permutations('0123', r=4):
        if ls[int(a1)] + ls[int(a2)] == ls[int(a3)] + ls[int(a4)]:
            return True
    return False

cnt = 0
for ls in data:
    c1 = max(ls) < (sum(ls) - max(ls))
    c2 = not(f(ls))
    if c1 and c2:
        cnt += 1
print(cnt)
# ans -> 2396