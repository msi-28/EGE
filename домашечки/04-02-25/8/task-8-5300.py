from itertools import permutations

alf = 'хочу в вуз'
cnt = 0
for s in set(permutations(alf)):
    s = ''.join(s)
    if s[0] != ' ' and s[-1] != ' ' and '  ' not in s:
        s = s.split()
        if len(s) == 3:
            cnt0 = 0
            for i in s:
                if i[0] == 'у':
                    cnt0 += 1
            if cnt0 == 0:
                cnt += 1
print(cnt)

# ans -> 75600
