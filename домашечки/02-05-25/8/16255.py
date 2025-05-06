from itertools import *

cnt = 0
for s in product('012345678', repeat=7):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = int(s[0])%2 == 0
    c2 = int(s[-1])%3!=0
    c3 = '6' in s
    if c0 and c1 and c2 and c3:
        cnt += 1

print(cnt)

# ans -> 827352