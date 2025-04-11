from itertools import *

cnt = 0
for s in product('01234', repeat=6):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s[1] == '3'
    if c0 and c1:
        cnt += 1
print(cnt)
# ans -> 2500