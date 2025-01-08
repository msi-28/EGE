from itertools import product

cnt = 0
for s in product('012345', repeat = 6):
    s = ''.join(s)
    c1 = s[0] != '0'
    for i in set(s):
        if int(i) % 2 != 0:
            s = s.replace(i, '*')
    c2 = '*0' not in s and '0*' not in s
    if c1 and c2:
        cnt += 1
print(cnt)