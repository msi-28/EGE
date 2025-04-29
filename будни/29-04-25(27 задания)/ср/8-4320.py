from itertools import *

cnt = 0
for s in set(permutations('01234567', r=6)):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = int(s, 8)%5 == 0
    for i in s:
        if int(i)%2 == 0:
            s = s.replace(i, '*')
        else:
            s = s.replace(i, '&')
    c2 = s == '*&*&*&' or s == '&*&*&*'
    if c0 and c1 and c2:
        cnt += 1
print(cnt)