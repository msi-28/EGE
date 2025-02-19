from itertools import permutations

cnt = 0
for s in permutations('0123456789', r=6):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = int(s) % 4 == 0
    for i in s:
        if int(i)%2 == 0:
            s = s.replace(i, '*')
    c2 = '**' not in s
    if c0 and c1 and c2:
        cnt += 1
print(cnt)

# ans -> 7440