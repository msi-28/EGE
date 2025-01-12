from itertools import *

def f(x,y,z,w):
    return (y <= x) or (not((x <= z) and (z <= x))) and (not w)

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
    table = [(0,0,0,a1), (a2,0,0,a3), (a4,a5,0,a6)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            c1 = [f(**dict(zip(p,t))) for t in table] == [0, 0, 0]
            if c1:
                print(''.join(p))

# ans -> wzxy