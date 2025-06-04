from itertools import *
from string import printable

alf = printable[:15]
cnt = 0
for s in product(alf, repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s.count('8') == 1
    c2 = len([i for i in s if int(i, 15) > 9]) >= 2
    if c0 and c1 and c2:
        cnt += 1
print(cnt)
# ans -> 83175