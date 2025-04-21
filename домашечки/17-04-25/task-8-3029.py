from itertools import *

cnt = 0
for s in product('012345678', repeat=7):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s[-1] not in '347'
    c2 = len([i for i in set(s) if i*3 in s]) == 0
    if c0 and c1 and c2:
        cnt += 1
print(cnt)