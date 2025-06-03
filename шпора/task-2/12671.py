from itertools import *

def f(x, y, z, w):
    return (not(x == (w and (not z)))) and (y == (x and (not w)))

for a1,a2,a3,a4,a5,a6, a7 in product([0,1], repeat = 7):
    table = [(a1,a2,0,a4), (a5,0,a6,0), (0,a7,1,0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(''.join(p))