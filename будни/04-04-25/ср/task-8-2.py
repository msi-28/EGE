from itertools import *

cnt = 0
for s in product('0123456', repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s.count('6') == 1
    c2 = sum(map(int,[i for i in s if int(i)%2 == 0])) < sum(map(int,[i for i in s if int(i)%2 != 0]))
    if c0 and c1 and c2:
        cnt += 1
print(cnt)