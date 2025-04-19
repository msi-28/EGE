from itertools import *

alf = sorted('ИНСТАВК')
cnt = 0
for s in product(alf, repeat=4):
    s = ''.join(s)
    if s[0] in 'НСТВК' and s[-1] in 'ИА':
        cnt += 1
        print(cnt, s)
    if s == 'НИКА':
        print(cnt)

# ans -> 231