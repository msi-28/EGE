from itertools import *
from string import printable
alf = printable[:25]

cnt = 0
for s in product(alf, repeat=4):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = len([i for i in s if int(i,25) <= 5]) <= 2
    for i in s:
        if int(i, 25) % 2 != 0:
            s = s.replace(i, '*')
    c2 = s.count('*') == 1
    if c0 and c1 and c2:
        cnt += 1
print(cnt)