from itertools import *
cnt = 0
alf = sorted('АРГУМЕНТ')
for s in product(alf, repeat=4):
    s = ''.join(s)
    c1 = len(set(s)) == len(s)
    c2 = ''.join(sorted(s)) == s
    cnt += 1
    if c1 and c2:
        print(cnt, s)

print(int('4567', 8)+1)