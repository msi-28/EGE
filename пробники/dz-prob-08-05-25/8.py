from itertools import *

cnt = 0
for s in product('0123456789', repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s[-1] not in '347'
    c2 = len([1 for i in s if i*3 in s]) == 0
    if c0 and c1 and c2:
        cnt += 1
print(cnt)