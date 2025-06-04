from itertools import *

cnt = 0
for s in product('01234567', repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = int(s[0])%2 == 0
    c2 = s[-1] not in '26'
    c3 = s.count('7') <= 2
    if c0 and c1 and c2 and c3:
        cnt += 1
print(cnt)
# ans -> 9135