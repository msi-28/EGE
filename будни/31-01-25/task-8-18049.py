from itertools import *

cnt = 0
for s in product('012345678', repeat=7):
    s = ''.join(s)
    c1 = s[0] not in '0246'
    c2 = s[-3:][0] != s[-3:][1] or s[-3:][1] != s[-3:][2] or  s[-3:][0] != s[-3:][2]
    if c1 and c2:
        cnt+=1
print(cnt)

# ans -> 2624400