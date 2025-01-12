from itertools import *

def f(x,y,w,z):
    return (x == (not z)) <= ((x or w) == y)

for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    table = [(0,a1,0,a2), (a3,a4,0,0), (a5,0,0,0)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            c1 = [f(**dict(zip(p, t))) for t in table] == [0,0,0]
            if c1:
                print(''.join(p))

# ans -> xwyz