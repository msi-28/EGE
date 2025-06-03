from itertools import *

cnt = 0
for s in product('0123456', repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    s1 = s
    for i in set(s):
        if int(i)%2 == 0:
            s1 = s1.replace(i, '*')
        else:
            s1 = s1.replace(i, '&')
    c2 = s1.count('**') >= 2
    c3 = '***' not in s1
    if c0 and c2 and c3:
        cnt += 1
print(cnt)

# ans -> 576