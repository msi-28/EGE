from itertools import *

alf = 'ABCDEF'
cnt = 0
for s in product(alf, repeat=6):
    s = ''.join(s)
    c1 = s[0] != 'A' and s[0] != 'E'
    c2 = s[-1] != 'A' and s[-1] != 'E'
    if c1 and c2:
        cnt += 1
print(cnt)

# ans -> 20736