from itertools import *

graph = 'CE EG GF FA AC CD DH AB BF'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans -> 18