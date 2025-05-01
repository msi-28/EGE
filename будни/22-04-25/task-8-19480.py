from itertools import *

alf = sorted('ПАРИЖАНКА')
cnt = 0
for s in set(permutations(alf)):
    s = ''.join(s)
    s = s.replace('И', "А")
    if s.count('АА') == 1 and s.count('ААА') == 0:
        cnt += 1
print(cnt)

# ans -> 28800