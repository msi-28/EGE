print('x y w z f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not(w <= (x ==( y or y))) and (z <= x)
                if f:
                    print(x,y,w,z,f)

# ------------------------------------------------

from itertools import *

def f(x,y,w,z):
    return not(w <= (x == (y or y))) and (z <= x)
for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
    table = [(a1,1,1,a2), (0,a3,a4,0), (a5,0,1,0)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,1]:
                print(''.join(p))