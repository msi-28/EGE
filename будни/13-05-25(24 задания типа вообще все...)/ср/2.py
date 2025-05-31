from itertools import *

def f(x,y,z,w):
    return (z <= w) and y and (not x)

for a1,a2,a3,a4,a5 in product([0, 1], repeat = 5):
    table = [(0,1,a1,0), (a2,0,a3,a4), (0,1,1,a5)]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,0]:
                print(''.join(p))