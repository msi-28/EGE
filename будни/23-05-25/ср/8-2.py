from itertools import *

cnt = 0
for s in product('0123456789', repeat=5):
    s = ''.join(s)
    if s[0] != '0':
        cnt += 1
        s1 = s
        for i in set(s):
            if int(i) % 2 == 0:
                s1 = s1.replace(i, '*')
            else:
                s1 = s1.replace(i, '&')
        if (s1 == '&*&*&' or s1 == '*&*&*') and cnt%15 == 0:
            print(cnt, s)

# ans -> 88950
