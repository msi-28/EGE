from itertools import product

cnt = 0
for s in product('ЯСНОВИДЕЦ', repeat=5):
    s = ''.join(s)
    c1 = s[0] in 'СНВДЦ' and s[-1] not in 'СНВДЦ'
    c2 = s.count(s[0]) == 1 and s.count(s[-1]) == 1
    if c1 and c2:
        cnt += 1
print(cnt)

# ans -> 6860