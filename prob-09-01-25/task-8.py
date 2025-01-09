from itertools import *

alf = 'ABCDEF'
cnt = 0
for s in product(alf, repeat=6):
    s = ''.join(s)
    c1 = s[0] != 'A'
    c2 = s[-1] != 'A'
    if c1 and c2:
        cnt += 1
print(cnt)

# ans -> 32400