from itertools import *

graph = 'AB BG GE EF FA AD FD DC EC CB'.split()
matrix = '457 567 45 136 123 247 126'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
# ans -> 22