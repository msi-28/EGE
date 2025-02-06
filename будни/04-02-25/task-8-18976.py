from itertools import *
from string import printable as p

alf = p[:20]
cnt = 0

for s in product(alf, repeat=5):
    s = ''.join(s)
    c1 = int(s[0], 20) + int(s[-1], 20) == 26
    for i in s:
        if i in alf[::2]:
            s = s.replace(i, '0')
        else:
            s = s.replace(i, '1')
    c2 =  s == '01010' or s == '10101'
    if c1 and c2:
        cnt += 1

print(cnt)
# ans -> 13000