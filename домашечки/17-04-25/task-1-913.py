from itertools import *

graph = 'AB BF FG GE AC CE BD DF CD'.split()
matrix = '235 146 145 236 137 247 56'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans -> 34