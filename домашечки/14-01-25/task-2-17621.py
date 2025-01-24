print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(x <= z) or (y == w) or y
                if not f:
                    print(x,y,z,w,int(f))

# ------------------------------------------------

from itertools import *

def f(x,y,z,w):
    return not(x <= z) or (y == w) or y

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
    table = [(1,0,a1,a2), (a3,1,0,a4), (0,a5,a6,a7)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [0,0,0]:
                print(''.join(p))

# ans -> zxyw