from itertools import product, repeat
from string import ascii_uppercase, digits

alf = digits + ascii_uppercase
gl_cnt = 0
for s in product(alf[:15], repeat=5):
    s = ''.join(s)
    cnt = 0
    c1 = s[0] != '0'
    c2 = s.count('8') == 1
    for i in s:
        if int(i, 15) > 9:
            cnt += 1
    c3 = cnt >= 2
    if c1 and c2 and c3:
        gl_cnt += 1
print(gl_cnt)