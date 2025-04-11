from itertools import *

cnt = 0
for s in product('ДГИАШЭ', repeat=5):
    s = ''.join(s)
    c1 = s[0] not in 'ИАЭ'
    c2 = s[-1] not in 'ДГШ'
    if c1 and c2:
        cnt += 1
print(cnt)

# ans -> 5832