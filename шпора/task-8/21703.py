from itertools import *

cnt = 0
alf = sorted('ПОБЕДА')
for s in product(alf, repeat=6):
    s = ''.join(s)
    c1 = s[0] == 'О'
    c2 = len(s) == len(set(s))
    cnt += 1
    if c1 and c2 and cnt%2 == 0:
        print(cnt)
# ans -> 3830