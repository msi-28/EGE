from itertools import *

cnt = 0
for s in product('котбус', repeat=8):
    s = ''.join(s)
    c1 = s[0] not in 'оу'
    c2 = 'кот' in s
    if c1 and c2:
        cnt += 1

print(cnt)

# 33516