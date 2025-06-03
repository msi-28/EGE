from itertools import *

graph = 'AD DE EG GC CF FA AB BE FB'.split()
matrix = '37 367 126 56 34 247 126'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
# ans -> 13 + 53 = 66