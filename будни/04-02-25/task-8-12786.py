from itertools import *

cnt = 0
alf = 'МАКАКА'
for s in set(permutations(alf, r=6)):
    s = ''.join(s)
    if 'АА' not in s and 'КК' not in s:
        cnt += 1
print(cnt)

# ans -> 120