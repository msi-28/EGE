from itertools import *

def f(x):
    P = 15<=x<=40
    Q = 21<=x<=63
    A = a1<=x<=a2
    return P <= ((Q and (not A)) <= (not P))
ls =[]
OX = [i/4 for i in range(10*4 , 65*4)]
for a1, a2 in combinations(OX, 2):
    if all(f(x) == 1 for x in OX):
        ls.append(a2-a1)
print(min(ls))
