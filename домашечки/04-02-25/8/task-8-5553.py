from itertools import permutations

alf = 'соточка'
cnt = 0
for s in set(permutations(alf)):
    s = ''.join(s)
    for i in 'оа':
        s = s.replace(i, '*')
    if '**' in s:
        cnt += 1
print(cnt)

# ans -> 1800