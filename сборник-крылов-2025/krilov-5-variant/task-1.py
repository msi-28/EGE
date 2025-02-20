from itertools import *

graph = 'AB BC CG GF FE EA BE CF CD DE'.split()
matrix = '457 357 25 17 1236 57 1246'.split()

print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans -> 34