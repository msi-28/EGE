from itertools import *

def f(x,y,w,z):
    return (x and z) or ((w <= x) == (z <= y))

for a1,a2,a3,a4,a5,a6 in product([0,1],repeat=6):
    table = [(a1,a2,a3,1,), (a4,a5,1,1), (a6,1,1,1)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            c1 = [f(**dict(zip(p, t))) for t in table] == [0,0,0]
            if c1:
                print(''.join(p))

# ans -> xzyw