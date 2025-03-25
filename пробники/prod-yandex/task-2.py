from itertools import *

def f(w, x, y, z):
    return w and (y == (z <= (x or y)))

for a1,a2,a3,a4,a5 in product([0, 1], repeat=5):
    table = [(a1,0,0,a2), (1, a3, 1, 0), (a4, a5, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,1]:
                print(''.join(p))

# ans -> wxyz