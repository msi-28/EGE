from itertools import *

cnt = 0
alf = 'КИДАЛА'
for s in set(permutations(alf, r=5)):
    s = ''.join(s)
    v = 0
    for i in s:
        if i*2 in s:
            v += 1
    if v == 0:
        cnt += 1
print(cnt)

# ans -> 120