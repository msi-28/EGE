from itertools import *

ans = 0
cnt = 0
for s in product('ИМНСУ', repeat=4):
    s = ''.join(s)
    cnt += 1
    for i in s:
        if i in 'ИУ':
            s = s.replace(i, '*')
        else:
            s = s.replace(i, '&')
        c1 = s.count('&') >= s.count('*')
        if c1:
            ans = cnt
print(ans)