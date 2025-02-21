from itertools import *

def f(w,x,y,z):
    return ((x <= z) <= w) or (not y)

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
    table = [(a1,a2,1,a3), (a4,0,a5,a6), (a7,1,0,0)]
    if len(set(table)) == len(table):
        for s in permutations('wxyz'):
            if [f(**dict(zip(s, t))) for t in table] == [0,0,0]:
                print(''.join(s))