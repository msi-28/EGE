from itertools import *

def f(a,b,c,d):
    return ((a and b) == (not(c))) and (b <= d)

table = [(1,0,0,0), (1,0,1,0), (1,0,1,1), (1,1,0,0)]
for p in permutations('abcd'):
    c1 = [f(**dict(zip(p, t))) for t in table] == [1,1,1,1]
    if c1:
        print(''.join(p))

# ans -> cadb