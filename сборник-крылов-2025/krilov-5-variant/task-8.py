from itertools import *

alf = 'АВИОРТФ'
n = 0
cnt = 0
for s in product(alf, repeat=6):
    s = ''.join(s)
    c1 = s[0] != 'О'
    c2 = s.count('Р') == 2
    n += 1
    if c1 and c2 and n%2 == 0:
        cnt += 1

print(cnt)
# ans -> 8640