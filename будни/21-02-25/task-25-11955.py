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

#      ans
#       |
#       v
# 122157574 918478
# 1021575394 7681018
# 1421575554 10688538
# 1821575714 13696058


