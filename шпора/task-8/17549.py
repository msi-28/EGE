from itertools import *
cnt = 0
alf = sorted('ФОКУС')
for s in product(alf, repeat=5):
    s = ''.join(s)
    cnt += 1
    if 'Ф' not in s and s.count('У') == 2:
        print(cnt)

# ans -> 2313