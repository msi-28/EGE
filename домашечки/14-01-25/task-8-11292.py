from itertools import product
from string import ascii_uppercase, digits

cnt = 0
alf = (digits + ascii_uppercase)[:16]
for s in product(alf, repeat=5):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s.count('6') == 2
    for i in s:
        if int(i,16) % 2 == 0 and i != '6':
            s = s.replace(i, '*')
    c2 = ('*6' not in s) and ('6*' not in s) and ('66' not in s)
    if c1 and c2 and c0:
        cnt += 1
print(cnt)

# ans -> 4352