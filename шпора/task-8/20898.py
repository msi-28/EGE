from itertools import *

cnt = 0
for s in product('012345678', repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s.count('0') == 1
    for i in s:
        if int(i)%2 != 0:
            s = s.replace(i, '&')
    c2 = '&0' not in s and '0&' not in s
    if c0 and c1 and c2:
        cnt += 1
print(cnt)

# ans -> 5120