from itertools import *

graph = 'AG GB BE EF FD DC CA BA FC'.split()
matrix = '246 16 57 15 347 127 356'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans -> 23