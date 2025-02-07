from itertools import *

graph = 'АБ БД ДЖ ЖЗ ЗЕ ЕГ ГВ ВБ ГД ЕЖ'.split()
matrix = '356 358 128 67 127 147 456 23'.split()
print(*range(1,9))
for i in permutations(''.join(sorted(set(''.join(graph))))):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

