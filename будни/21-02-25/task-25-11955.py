from string import digits as d
from itertools import product
q = d[::2]
z = d[1::2]
ans = []
for r in range(4):
    for B in product(z, repeat=r):
        B = ''.join(B)
        for A in q:
            num = int(f'1{A}2157{B}4')
            if num%133 == 0 and num <= 10**10:
                ans.append([num, num//133])

for e in sorted(ans):
    print(*e)
# _____________________________________
# решение через fnmatch

from fnmatch import fnmatch as fn

for i in range(1021574 - 1021574%133, 10**10, 133):
    if fn(str(i), '1[02468]2157[ 13579][ 13579][ 13579]4'):
        print(i, i//133)