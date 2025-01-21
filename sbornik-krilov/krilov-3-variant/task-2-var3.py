from itertools import *

def f(x,y,z,w):
    return not(x <= y) or (not z == (w <= x)) or w

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
    table = [(a1,1,a2,0), (a3,a4,0,1), (a5,a6,1,a7)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            c1 = [f(**dict(zip(p, t))) for t in table] == [0,0,0]
            if c1:
                print(''.join(p))

# ans -> wzxy