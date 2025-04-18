from itertools import *

cnt = 0
for s in product('01234', repeat=6):
    s = ''.join(s)
    c1 = s[0] == '3'
    c2 = int(s, 5)%2 == 0
    if c1 and c2:
        cnt += 1
        print(s)
print(cnt)
# ans -> 1562